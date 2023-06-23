#!/usr/bin/python3
# Fabric script for deploying an archive to web servers.abs
from fabric.api import local, env, put, run
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['54.163.201.110', '54.227.84.117']


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
    if not path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web servers
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension
        filename = archive_path.split('/')[-1]
        name = filename.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(name))

        # Extract the contents of the archive file to the specified folder on the web server.
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, name))

        # Executes a system command to remove a file located in the / tmp / directory.
        run("sudo rm /tmp/{}".format(filename))

        # Executes a system command to recursively copy files and directories from one location to another.
        run("sudo cp -rf /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(name, name))

        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(
            name))
        return True
    except Exception:
        return False
