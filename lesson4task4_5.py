# -*- coding: utf-8 -*-
# !/usr/bin/python3

from lesson4task2_3 import currency_rates
from sys import argv

if len(argv) > 1:
    for item in argv[1:]:
        print(f'На {currency_rates(item)[0]} : {currency_rates(item)[1].get("nominal")} {currency_rates(item)[1].get("name")} стоит {currency_rates(item)[1].get("value")} рублей.')
else:
    print(currency_rates()['date'])
    for keys, vlaute in currency_rates().items():
        if keys != 'date':
            print(f'{keys} - {vlaute["value"]} рублей за {vlaute["nominal"]} {vlaute["name"]}')
