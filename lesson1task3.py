# -*- coding: utf-8 -*-
#!/usr/bin/python3

for number in range(1, 101):
    if number // 10 == 1 or number % 10 > 4 or number % 10 == 0:
        print('{} процентов'.format(number))
    elif 1 < number % 10 < 5:
        print('{} процента'.format(number))
    else:
        print('{} процент'.format(number))
