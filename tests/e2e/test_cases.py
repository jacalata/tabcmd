import subprocess
import sys
import typing
import unittest

import e2e_vars
import setup_exe



def _test_command(test_args: list[str]):
    # this will raise an exception if it gets a non-zero return code
    # that should bubble up and fail the test?
    calling_args = [setup_exe.exe] + test_args
    print(calling_args)
    return subprocess.check_call(calling_args)


def create_delete_group():
    command = "creategroup"
    arguments = [command, e2e_vars.group_name]
    _test_command(arguments)

    # PAUSE FOR THOUGHT ?

    command = "deletegroup"
    arguments = [command, e2e_vars.group_name]
    _test_command(arguments)


if __name__ == "__main__":
    # expect that we are already logged in because user called setup_exe
    create_delete_group()