"""Credential-free smoke test for an installed or frozen tabcmd.

usage: smoke.py --expect-version X.Y.Z -- <command to run tabcmd>

Run from a directory outside the source tree. Every check runs the real executable
the way a user would, so missing hidden imports, data files and certificates fail here.
"""

import argparse
import re
import subprocess
import sys

BAD_OUTPUT = ["ModuleNotFoundError", "ImportError", "No module named", "CERTIFICATE_VERIFY_FAILED", "Traceback"]
failures: list[str] = []


def run(base, args, timeout=120):
    proc = subprocess.run(
        base + args, capture_output=True, text=True, timeout=timeout, encoding="utf-8", errors="replace"
    )
    return proc.returncode, proc.stdout + proc.stderr


def expect(ok, message):
    print("{}: {}".format("ok  " if ok else "FAIL", message))
    if not ok:
        failures.append(message)


def list_commands(base):
    _, out = run(base, ["help"])
    section = out.split("List of Tabcmd commands", 1)[-1]
    names = re.findall(r"^    ([a-z]+)\s{2,}\S", section, re.MULTILINE)
    return [n for n in names if n != "help"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--expect-version", required=True)
    parser.add_argument("base", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    base = [a for a in args.base if a != "--"]

    rc, out = run(base, ["--version"])
    expect(
        rc == 0 and args.expect_version in out,
        "--version reports {} (rc={}): {!r}".format(args.expect_version, rc, out.strip()),
    )

    rc, out = run(base, [])
    expect(rc == 0 and "List of Tabcmd commands" in out, "no arguments prints help (rc={})".format(rc))

    commands = list_commands(base)
    expect(len(commands) >= 20, "help lists commands: {}".format(len(commands)))
    for name in commands:
        rc, out = run(base, [name, "-h"])
        bad = [b for b in BAD_OUTPUT if b in out]
        expect(
            rc == 0 and "usage: tabcmd {}".format(name) in out and not bad,
            "{} -h (rc={}, bad={})".format(name, rc, bad),
        )

    # An unreachable host must fail as a connection error, not as an import or ssl-bundle error.
    rc, out = run(
        base, ["login", "-s", "https://nonexistent.invalid", "--token-name", "x", "--token-value", "y", "--no-prompt"]
    )
    bad = [b for b in BAD_OUTPUT if b in out]
    expect(
        rc != 0 and "nonexistent.invalid" in out and not bad,
        "login to unresolvable host fails cleanly (rc={}, bad={})".format(rc, bad),
    )

    # A reachable HTTPS host that is not a Tableau Server proves the bundled CA store can validate a real certificate.
    rc, out = run(
        base, ["login", "-s", "https://example.com", "--token-name", "x", "--token-value", "y", "--no-prompt"]
    )
    expect(
        "CERTIFICATE_VERIFY_FAILED" not in out and "SSLError" not in out,
        "TLS handshake to example.com succeeds (rc={})".format(rc),
    )

    # Every bundled .mo catalog must load: a missing one falls back to English. --language must follow the
    # subcommand, because the subcommand parser resets a value given before it.
    for lang in ["de", "es", "fr", "it", "ja", "ko", "pt", "sv", "zh"]:
        rc, out = run(
            base,
            [
                "login",
                "--language",
                lang,
                "-s",
                "https://nonexistent.invalid",
                "--token-name",
                "x",
                "--token-value",
                "y",
                "--no-prompt",
            ],
        )
        expect(
            "Connecting to the server" not in out and "Failed to load language" not in out,
            "--language {} output is translated".format(lang),
        )

    print("\n{} failure(s)".format(len(failures)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
