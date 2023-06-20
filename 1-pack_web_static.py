#!/usr/bin/python3
"""Fabric script that generates a .tgz archive."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the web static folder"""
    local("mkdir -p versions")

    # Generate the archive name using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive
    result = local("tar-czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
