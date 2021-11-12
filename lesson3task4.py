# -*- coding: utf-8 -*-
# !/usr/bin/python3


def thesaurus_adv(*args: str, sort=False):
    if sort:
        fullname_dict = dict(map(lambda fn: (fn, {}), sorted(list(map(lambda pref: pref[pref.find(' ') + 1], args)))))
        for sn_key, val in fullname_dict.items():
            name_list = sorted(list(filter(lambda sn: sn[sn.find(' ') + 1] == sn_key, args)))
            name_dict = dict(map(lambda nam: (nam[0], []), name_list))
            for name in name_list:
                name_dict.get(name[0]).append(name)
            val.update(name_dict)
    else:
        fullname_dict = dict(map(lambda fn: (fn, {}), list(map(lambda pref: pref[pref.find(' ') + 1], args))))
        for sn_key, val in fullname_dict.items():
            name_list = list(filter(lambda sn: sn[sn.find(' ') + 1] == sn_key, args))
            name_dict = dict(map(lambda nam: (nam[0], []), name_list))
            for name in name_list:
                name_dict.get(name[0]).append(name)
            val.update(name_dict)
    return fullname_dict
