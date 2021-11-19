# -*- coding: utf-8 -*-
# !/usr/bin/python3


def yield_gen(count=1):
    for number in range(1, count+1):
        if number % 2:
            yield number

print(*(number for number in range(1, int(input('Y='))) if number % 2))

print(*yield_gen(int(input('X='))))

