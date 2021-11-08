# -*- coding: utf-8 -*-
#!/usr/bin/python3

from random import randint                          # Данный блок введён потому, что мне лень вводить список в ручную
from random import uniform                          #
price_list = []                                     #
for i in range(10, randint(20, 200)):               #
    price_list.append(round(uniform(0, 100), 2))    #

# A
for price_id, price in enumerate(price_list, 1):
    price_ruble = round(price // 1)
    price_penny = round(price % 1 * 100)
    if price_id != len(price_list):
        print(f'{price_ruble} руб {price_penny:02d} коп', end=', ')
    else:
        print(f'{price_ruble} руб {price_penny:02d} коп')

# B & D
print(f'{price_list}\n{id(price_list)}')
price_list.sort()
print(f'{price_list}\n{id(price_list)}')
top = int(input('Сколько чисел вывести (0 = все): '))
for price_id, price in enumerate(price_list[-top:], 1):
    price_ruble = round(price // 1)
    price_penny = round(price % 1 * 100)
    if price_id != len(price_list[-top:]):
        print(f'{price_ruble} руб {price_penny:02d} коп', end=', ')
    else:
        print(f'{price_ruble} руб {price_penny:02d} коп')

# C
price_list.sort(reverse=True)
for price_id, price in enumerate(price_list, 1):
    price_ruble = round(price // 1)
    price_penny = round(price % 1 * 100)
    if price_id != len(price_list):
        print(f'{price_ruble} руб {price_penny:02d} коп', end=', ')
    else:
        print(f'{price_ruble} руб {price_penny:02d} коп')