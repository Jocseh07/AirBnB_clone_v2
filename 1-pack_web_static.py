#!/usr/bin/python3
# Fabric script to generate a .tgz file from the contents of the web_static folder

from fabric.api import local
from datetime import datetime

def do_pack():
    """Create a tar.gz archive.
    """
    date = datetime.now()
    tgz = "versions/web_static_{}{}{}{}{}{}.tgz".format(\
        date.year, date.month, date.day, date.hour, date.minute, date.second)
    if local("tar -czvf {} web_static".format(tgz)).failed is True:
        return None
    return tgz