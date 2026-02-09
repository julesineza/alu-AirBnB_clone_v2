#!/usr/bin/python3
"""packing"""
from fabric.api import local
from datetime import datetime
import os 

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.isdir("versions"):

            local("mkdir -p versions")

            now = datetime.now()
            archive_name = f"web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz"

            archive_path=f"/versions/{archive_name}"

            result =local(f"tar -cvzf {archive_path} webstatic")

        if result.succeeded:
            archive_size = os.path.getsize(archive_path)
            print("web_static packed: {} -> {}Bytes".format(
                archive_path, archive_size))
            return archive_path
        else:
            return None
    except Exception :
        return  None 

