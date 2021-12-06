# -*- coding: utf-8 -*-
# !/usr/bin/python3


from functools import wraps

def logger(func):
    @wraps(func)
    def log_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}(', end='')
        for i in args:
            print(f'{i}: {type(i)}', end=', ')
        for k, v in kwargs.items():
            print(f' variable {k}={v}: {type(v)}', end='')
        print(')')
        print(func.__doc__)
        return result
    return log_func


@logger
def calc_cube(*xx, **xxx):
    return (x ** 3 for x in xx), xxx

