# -*- coding: utf-8 -*-
# !/usr/bin/python3

from pprint import pprint

n_list = "Иван", "Мария", "Петр", "Илья"

def thesaurus(*args: str, sort=False):
    if sort:
        names = sorted(args)
    else:
        names = args
    name_dict = {}
    for first_name in names:
        if name_dict.get(first_name[0]) is None:
            name_dict.setdefault(first_name[0], [first_name])
        else:
            name_dict.get(first_name[0]).append(first_name)
    return name_dict


