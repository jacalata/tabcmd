"""Checks the contents of built distributions: usage: check_dist.py <dist dir>

Fails if the wheel or sdist is missing localized string catalogs or subpackages.
"""

import sys
import tarfile
import zipfile
from pathlib import Path

LOCALES = ["de", "en", "es", "fr", "ga", "it", "ja", "ko", "pt", "sv", "zh"]
REQUIRED_PACKAGES = ["tabcmd/commands", "tabcmd/execution"]


def check(kind: str, names: list) -> list:
    problems = []
    for lang in LOCALES:
        if not any(n.endswith("tabcmd/locales/{}/LC_MESSAGES/tabcmd.mo".format(lang)) for n in names):
            problems.append("{}: missing {} catalog".format(kind, lang))
    for pkg in REQUIRED_PACKAGES:
        if not any("{}/__init__.py".format(pkg) in n for n in names):
            problems.append("{}: missing package {}".format(kind, pkg))
    return problems


def main(dist_dir: str) -> int:
    dist = Path(dist_dir)
    wheels = list(dist.glob("*.whl"))
    sdists = list(dist.glob("*.tar.gz"))
    if len(wheels) != 1 or len(sdists) != 1:
        print("expected exactly one wheel and one sdist in {}, found {} and {}".format(dist, wheels, sdists))
        return 1

    problems = []
    with zipfile.ZipFile(wheels[0]) as z:
        problems += check("wheel", z.namelist())
    with tarfile.open(sdists[0]) as t:
        problems += check("sdist", t.getnames())

    for p in problems:
        print("FAIL:", p)
    if not problems:
        print("OK: {} and {} contain all catalogs and subpackages".format(wheels[0].name, sdists[0].name))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
