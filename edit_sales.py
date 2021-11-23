# -*- coding: utf-8 -*-
# !/usr/bin/python3


from lesson6task6_7 import edit_record
from sys import argv

if len(argv) != 3:
    print(f'Использование скрипта:'
          f'{argv[0]} <номер_строки> <новое значение>')
else:
    try:
        edit_record('bakery.csv', int(argv[1]), argv[2])
    except ValueError as error:
        print(f'Нужно ввести номер строки. {error}')
