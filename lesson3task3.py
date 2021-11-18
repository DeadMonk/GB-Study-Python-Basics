# -*- coding: utf-8 -*-
# !/usr/bin/python3


def thesaurus(*args: str, sort=False):
    if sort:
        name_dict = dict(map(lambda nam: (nam[0], []), sorted(args)))
        for name in sorted(args):
            name_dict.get(name[0]).append(name)
    else:
        name_dict = dict(map(lambda nam: (nam[0], []), args))
        for name in args:
            name_dict.get(name[0]).append(name)
    return name_dict
