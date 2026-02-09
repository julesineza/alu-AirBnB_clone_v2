#!/usr/bin/python3
"""creates and distributes an archive to your web servers,
using the function deploy"""
import importlib

pack_module = importlib.import_module("1-pack_web_static")
deploy_module = importlib.import_module("2-do_deploy_web_static")
do_pack = pack_module.do_pack
do_deploy = deploy_module.do_deploy

def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)