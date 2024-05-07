#!/usr/bin/python3
# delete out of date archives using do_clean

from fabric.api import *
import os

env.hosts = ["100.25.149.16", "100.25.146.118"]


def do_clean(number=0):
    """Delete out of date archives.

    Args:
        number (int, optional): number to keep. Defaults to 0.
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    files = os.listdir("versions")
    files = sorted(files)
    for _ in range(number):
        files.pop()
    with lcd("versions"):
        for a in files:
            local("rm ./{}".format(a))

    with cd("/data/web_static/releases"):
        all = run("ls -tr").split()
        for _ in range(number):
            all.pop()
        for a in all:
            run("rm -rf ./{}".format(a))
