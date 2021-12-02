# -*- coding: utf-8 -*-
# !/usr/bin/python3


from lesson6task6_7 import read_records, read_record, index_lines
from sys import argv

if len(argv) == 1:
    print(read_record('bakery.csv'))
elif len(argv) == 2:
    try:
        start = int(argv[1])
        print(''.join(read_records('bakery.csv', start)))
    except ValueError as error:
        print(f'Нужно ввести номер строки. {error}')
else:
    try:
        start = int(argv[1])
        end = int(argv[2])
        if start == end:
            print(read_record('bakery.csv', start), end='')
        else:
            print(''.join(read_records('bakery.csv', start, end)), end='')
    except ValueError as error:
        print(f'Нужно ввести номер строки. {error}')
