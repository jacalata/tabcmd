import os
import subprocess
import sys
import typing
import unittest

import credentials

our_program = "tabcmd.exe"
launch_path = os.path.join("..", "..", "dist", "tabcmd")
exe = os.path.join(launch_path, our_program)

def login():
    # --server, --site, --username, --password 
    args = [exe, "login", "--server", credentials.SERVER_URL, "--site", credentials.SITE_NAME, 
    "--token", credentials.PAT, "--token-name", credentials.PAT_NAME, "--no-certcheck"]
    print(args)
    return subprocess.check_call(args,  stderr=subprocess.STDOUT, shell=True)

if __name__ == "__main__":
    print("script is running in:")
    subprocess.check_call(["chdir"], shell=True)
    print("expecting built executable to be in " + launch_path + ":")
    subprocess.check_call(["dir", launch_path], shell=True)
    
    print("running", our_program)
    login()