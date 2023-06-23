#!/usr/bin/python3
# Fabric script for deploying an archive to web servers.abs



env.user = 'ubuntu'
env.hosts = [ '54.163.201.110', '54.227.84.117']


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

        #Executes a system command to remove a file located in the / tmp / directory.
        run("sudo rm /tmp/{}".format(filename))

        #Executes a system command to recursively copy files and directories from one location to another.
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
