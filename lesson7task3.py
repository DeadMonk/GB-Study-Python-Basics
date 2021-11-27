# -*- coding: utf-8 -*-
# !/usr/bin/python3


import os
import shutil


def copy_templates(search_dir: str):
    tdir = os.path.join(search_dir, 'templates')
    if not os.path.exists(tdir):
        os.mkdir(tdir)
    for r, d, f in os.walk(search_dir):
        if '.html' in ''.join(f):
            sdir = os.path.join(tdir, r.split('/')[-1])
            if r != sdir:
                shutil.copytree(r, sdir, dirs_exist_ok=True)
            print(r, sdir)

copy_templates('my_project')