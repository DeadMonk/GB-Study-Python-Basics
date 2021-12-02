# -*- coding: utf-8 -*-
# !/usr/bin/python3

from sys import argv
from itertools import zip_longest
from json import dump


result_dict = {}
with open('users.csv', 'r') as ufile, open('hobby.csv', 'r') as hfile, open('dict.json', 'w') as dfile:
    ulen = sum(1 for _ in ufile)
    hlen = sum(1 for _ in hfile)
    hfile.seek(0)
    ufile.seek(0)
    if ulen < hlen:
        exit(1)
    for user, hobby in zip_longest(ufile, hfile):
        result_dict[user.strip()] = hobby.strip() if hobby else hobby
    dump(result_dict, dfile, ensure_ascii=False)


if len(argv[1:]) < 3:
    print('Не указаны файлы')
    exit(1)

with open(argv[1], 'r') as ufile, open(argv[2], 'r') as hfile, open(argv[3], 'w') as uhfile:
    ulen = sum(1 for line in ufile)
    hlen = sum(1 for line in hfile)
    hfile.seek(0)
    ufile.seek(0)
    if ulen < hlen:
        exit(1)
    for user, hobby in zip_longest(ufile, hfile):
        print(f'{user.strip()}: {hobby.strip() if hobby else hobby}', file=uhfile)
