#!/usr/bin/python3
# Fabric script to generate a .tgz file from the contents of the web_static

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """Create a tar.gz archive.
    """
    date = datetime.now()
    tgz = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day, date.hour, date.minute, date.second)
    if isdir("versions") is False:
        if local("mkdir versions").failed is True:
            return None
    if local("tar -czvf {} web_static".format(tgz)).failed is True:
        return None
    return tgz
