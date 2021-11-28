# -*- coding: utf-8 -*-
# !/usr/bin/python3


import os
import json

def stat_files(dir_name: str, extensions=True):
    mfs = 0
    file_dict = {}
    result_dict = {}
    for r, d, f in os.walk(dir_name):
        for fn in f:
            mfs = max(mfs, os.stat(os.path.join(r, fn)).st_size)
            file_dict.setdefault(fn.split('.')[-1], [])
            file_dict[fn.split('.')[-1]].append(os.stat(os.path.join(r, fn)).st_size)
    for p in range(1, len(str(mfs)) + 1):
        files_count = 0
        ext_list = []
        for ext, size in file_dict.items():
            tmp_fc = files_count
            if p != 1:
                files_count += sum(1 for i in size if 10**(p-1) < i <= 10**p)
            else:
                files_count += sum(1 for i in size if i <= 10**p)
            if files_count - tmp_fc > 0:
                ext_list.append(ext)
        result_dict.setdefault(10 ** p, (files_count, ext_list))
    if extensions:
        return result_dict
    else:
        shot_result = {}
        for k, v in result_dict.items():
            shot_result.setdefault(k, v[0])
        return shot_result

print(stat_files('.', extensions=False))
print(stat_files('.'))

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as jfile:
    json.dump(stat_files('.'), jfile)