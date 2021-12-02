# -*- coding: utf-8 -*-
# !/usr/bin/python3


import os

project_dict = {'name': 'my_project',
                'type': 'dir',
                'comp': [{'name': 'settings',
                          'type': 'dir',
                          'comp': [{'name': '__init__.py',
                                    'type': 'file'},
                                   {'name': 'dev.py',
                                    'type': 'file'},
                                   {'name': 'prod.py',
                                    'type': 'file'}]},
                         {'name': 'mainapp',
                          'type': 'dir',
                          'comp': [{'name': '__init__.py',
                                    'type': 'file'},
                                   {'name': 'models.py',
                                    'type': 'file'},
                                   {'name': 'views.py',
                                    'type': 'file'},
                                   {'name': 'templates',
                                    'type': 'dir',
                                    'comp': [{'name': 'mainapp',
                                              'type': 'dir',
                                              'comp': [{'name': 'base.html',
                                                        'type': 'file'},
                                                       {'name': 'index.html',
                                                        'type': 'file'}]}]}]},
                         {'name': 'authapp',
                          'type': 'dir',
                          'comp': [{'name': '__init__.py',
                                    'type': 'file'},
                                   {'name': 'models.py',
                                    'type': 'file'},
                                   {'name': 'views.py',
                                    'type': 'file'},
                                   {'name': 'templates',
                                    'type': 'dir',
                                    'comp': [{'name': 'authapp',
                                              'type': 'dir',
                                              'comp':[{'name': 'base.html',
                                                       'type': 'file'},
                                                      {'name': 'index.html',
                                                       'type': 'file'}]}]}]}]}

def mk_yaml(yaml_file, tree_dict: dict, level=0):
    if level == 0:
        element_str = tree_dict['name']
    else:
        element_str = '  ' * (level - 1) + '- ' + tree_dict['name']
    if tree_dict['type'] == 'dir':
        element_str += ':'
    print(element_str, file=yaml_file)
    if tree_dict.get('comp'):
        for comp in tree_dict['comp']:
            mk_yaml(yaml_file, comp, level=level + 1)

def pars_yaml(yaml_file):
    def mk_dir_safe(dir_name: str):
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print(f'Директория {os.path.join(os.getcwd(), dir_name)} уже существует.')
    def mk_file_safe(file_name: str):
        try:
            os.mknod(line[ssymbol:].strip())
        except FileExistsError:
            print(f'Файл {os.path.join(os.getcwd(), file_name)} уже существует.')
    level = 0
    for line in yaml_file:
        ssymbol = line.find('- ') + 2
        if line.find('- ') == -1:
            mk_dir_safe(line.strip()[:-1])
            os.chdir(line.strip()[:-1])
        else:
            if level == line.find('-') // 2:
                if line[ssymbol:].strip()[-1] == ':':
                    mk_dir_safe(line[ssymbol:].strip()[:-1])
                    os.chdir(line[ssymbol:].strip()[:-1])
                    level += 1
                else:
                    mk_file_safe(line[ssymbol:].strip())
            elif level != line.find('- ') // 2:
                diff_lvl = level - line.find('- ') // 2
                os.chdir('../' * diff_lvl)
                level = level - diff_lvl
                if line[ssymbol:].strip()[-1] == ':':
                    mk_dir_safe(line[ssymbol:].strip()[:-1])
                    os.chdir(line[ssymbol:].strip()[:-1])
                    level += 1
                else:
                    mk_file_safe(line[ssymbol:].strip())

with open('config.yaml', 'w', encoding='utf-8') as yfile:
     mk_yaml(yfile, project_dict)

with open('config.yaml', 'r', encoding='utf-8') as yfile:
    pars_yaml(yfile)