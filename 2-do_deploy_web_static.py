#!/usr/bin/python3
# Fabric script for deploying an archive to web servers.abs
from fabric.api import local, env, put, run
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['3.90.229.110', '3.88.90.214']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""

    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filename))
    if os.path.exists(filename):
        return filename
    return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):

        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            filename, name))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo cp -rf /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(
            name))
        # Create 'hbnb_static' directory
        if not isdir("/var/www/html/hbnb_static"):
            run("sudo mkdir -p /var/www/html/hbnb_static")

        # Sync 'hbnb_static' with 'current'
        run("sudo cp -r /data/web_static/current/* /var/www/html/hbnb_static/")

        print("New version deployed!")
        return True
    except Exception:
        return False
