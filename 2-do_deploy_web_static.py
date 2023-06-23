#!/usr/bin/python3
"""
Script for distributing an archive to web servers
"""

from fabric.api import env, put, run, local
from os.path import exists, isdir
import os.path
import re

# Set the username and host for SSH connection to the server
env.user = 'ubuntu'
env.hosts = ['3.90.229.110', '3.88.90.214']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes the archive to web servers
    """
    # Check if the archive file exists
    if not exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Uncompress the archive to a folder
    filename = re.search(r'[^/]+$', archive_path).group(0)
    folder = "/data/web_static/releases/{}".format(
        os.path.splitext(filename)[0])

    # Create the folder if it doesn't exist
    if not exists(folder):
        run("mkdir -p {}".format(folder))

    # Extract files from the archive
    run("tar -xzf /tmp/{} -C {}".format(filename, folder))

    # Remove the archive from the web server
    run("rm /tmp/{}".format(filename))

    # Move all files from web_static to the new folder
    run("mv {}/web_static/* {}".format(folder, folder))

    # Remove the web_static folder
    run("rm -rf {}/web_static".format(folder))

    # Delete the symbolic link
    run("rm -rf /data/web_static/current")

    # Create a new symbolic link
    run("ln -s {} /data/web_static/current".format(folder))

    # Create the 'hbnb_static' directory if it doesn't exist
    if not isdir("/var/www/html/hbnb_static"):
        run("sudo mkdir -p /var/www/html/hbnb_static")

    # Sync 'hbnb_static' with 'current'
    run("sudo cp -r /data/web_static/current/* /var/www/html/hbnb_static/")

    print("New version successfully deployed!")
    return True
