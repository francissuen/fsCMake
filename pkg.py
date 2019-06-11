""" Copyright (c) 2019, F.S.. All rights reserved. """
import os
import tarfile
import shutil


if __name__ == "__main__":
    pkg_files = ['CMakeLists.txt', 'src_pkg.py.in', 'fs_proj.xml.in',
                 'build.py', 'build.sh']
    pkg_name = 'fsCMake'
    if os.path.isdir(pkg_name):
        shutil.rmtree(pkg_name)
    os.mkdir(pkg_name)
    for pkg_file in pkg_files:
        shutil.copy(pkg_file, pkg_name)
        
    pkg_path = 'fsCMake.tar.xz'
    if os.path.isfile(pkg_path):
        os.remove(pkg_path)
    with tarfile.open(pkg_path, 'x:xz') as f:
        f.add(pkg_name)
        f.close()
