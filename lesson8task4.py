# -*- coding: utf-8 -*-
# !/usr/bin/python3

from inspect import getsource

def val_checker(callback):
    def _val_checker(func):
        def check_func(arg):
            if callback(arg):
                return func(arg)
            else:
                raise ValueError(f'Не соответствует условию. {getsource(callback)}')
        return check_func
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(-2))