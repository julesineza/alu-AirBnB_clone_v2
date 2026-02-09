#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
from fabric.api import put, run, env, local
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Extract filename and name without extension
        file_name = archive_path.split("/")[-1]
        name_no_ext = file_name.split(".")[0]
        release_path = "/data/web_static/releases/{}".format(name_no_ext)

        # Upload archive to /tmp/ on the server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create the release directory
        run("mkdir -p {}".format(release_path))

        # Uncompress archive to the release directory
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))

        # Delete the archive from the server
        run("rm /tmp/{}".format(file_name))

        # Move contents out of the web_static subfolder
        run("mv {}/web_static/* {}".format(release_path, release_path))

        # Remove the now-empty web_static subfolder
        run("rm -rf {}/web_static".format(release_path))

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True

    except Exception:
        return False