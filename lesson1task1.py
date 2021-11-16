# -*- coding: utf-8 -*-
#!/usr/bin/python3

duration = int(input('Введите количество секунд: '))
divisor_list = [86400, 3600, 60, 1]
unit_list = ['дн', 'час', 'мин', 'сек']
result_string = ''
for divisor_id, divisor in enumerate(divisor_list):
    result = duration // divisor
    duration = duration % divisor
    if result == 0:
        continue
    result_string += '{} {} '.format(result, unit_list[divisor_id])
print(result_string)