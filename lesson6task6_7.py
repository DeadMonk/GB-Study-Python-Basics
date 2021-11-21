# -*- coding: utf-8 -*-
# !/usr/bin/python3


def add_record(file_name: str, record):
    with open(file_name, a, encoding='utf-8') as dfile:
        dfile.write(record)

add_record('test.csv', 5123.5)
