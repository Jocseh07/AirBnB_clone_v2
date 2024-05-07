#!/usr/bin/python3
# Fabric script to generate a .tgz file from the contents of the web_static

import os.path
from datetime import datetime
from os.path import isdir

from fabric.api import env, local, put, run

env.hosts = ["100.25.149.16", "100.25.146.118"]


def do_pack():
    """Create a tar.gz archive."""
    date = datetime.now()
    tgz = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day, date.hour, date.minute, date.second
    )
    if isdir("versions") is False:
        if local("mkdir versions").failed is True:
            return None
    if local("tar -czvf {} web_static".format(tgz)).failed is True:
        return None
    return tgz


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if os.path.isfile(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    name = filename.split(".")[0]

    if put(archive_path, "/tmp/{}".format(filename)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(
            name)).failed is True:
        return False
    if (
        run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                filename, name)
        ).failed
        is True
    ):
        return False
    if run("rm /tmp/{}".format(filename)).failed is True:
        return False
    if (
        run(
            "mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(
                name, name
            )
        ).failed
        is True
    ):
        return False
    if (
        run("rm -rf  /data/web_static/releases/{}/web_static".format(
            name)).failed
        is True
    ):
        return False
    if run("rm -rf  /data/web_static/current").failed is True:
        return False
    if (
        run(
            "ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)
        ).failed
        is True
    ):
        return False
    return True


def deploy():
    filename = do_pack()
    """Creates and distributes an archive to your web."""
    if filename is None:
        return False
    return do_deploy(filename)
