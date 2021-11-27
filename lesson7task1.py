# -*- coding: utf-8 -*-
# !/usr/bin/python3


import os
import json

project_dict = {'name': 'my_project',
                'type': 'dir',
                'comp': [{'name': 'settings', 'type': 'dir'},
                         {'name': 'mainapp', 'type': 'dir'},
                         {'name': 'adminapp', 'type': 'dir'},
                         {'name': 'authapp', 'type': 'dir'}]}


def mk_tree(tree_dict: dict):
    if tree_dict['type'] == 'dir':
        os.mkdir(tree_dict['name'])
    elif tree_dict['type'] == 'file':
        os.mknod(tree_dict['name'])
    if tree_dict.get('comp'):
        os.chdir(tree_dict['name'])
        for comp in tree_dict['comp']:
            mk_tree(comp)
        os.chdir('..')


with open('project.json', 'w') as jfile:
    json.dump(project_dict, jfile, ensure_ascii=False)


