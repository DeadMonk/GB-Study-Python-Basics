# -*- coding: utf-8 -*-
# !/usr/bin/python3

from lesson3task3 import thesaurus

def thesaurus_adv(*args: str, sort=False):
    fio_dict = {}
    fio_list = args
    if sort:
        tmp_list = []
        for full_name in args:
            tmp_list.append(full_name[full_name.find(' ') + 1])
        tmp_list.sort()
        for leter in tmp_list:
            fio_dict.setdefault(leter, {})
        fio_list = sorted(args)
    for full_name in fio_list:
        if fio_dict.get(full_name[full_name.find(' ') + 1]) == None:
            fio_dict.setdefault(full_name[full_name.find(' ') + 1], thesaurus(full_name))
        else:
            if full_name[0] in fio_dict.get(full_name[full_name.find(' ') + 1]).keys():
                fio_dict.get(full_name[full_name.find(' ') + 1]).get(full_name[0]).append(full_name)
            else:
                fio_dict.get(full_name[full_name.find(' ') + 1]).update({full_name[0]: full_name})
    return fio_dict




