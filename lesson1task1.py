# -*- coding: utf-8 -*-
#!/usr/bin/python3

duration = int(input('Введите количество секунд: '))

if duration >= 86400:
    print(duration // 86400, 'дн', (duration % 86400) // 3600, 'час', ((duration % 86400) % 3600) // 60, 'мин', duration % 60, 'сек')
elif duration >= 3600:
    print(duration // 3600, 'час', (duration % 3600) // 60, 'мин', (duration % 3600) % 60, 'сек')
elif duration >= 60:
    print(duration // 60, 'мин', duration % 60, 'сек')
else:
    print(duration, 'сек')

divisor_list = [86400, 3600, 60, 1]
unit_list = [ ' дн, ', ' час, ', ' мин, ', ' сек']
result_list = []
result_string = ''
for divisor_id in range(len(divisor_list)):
    result_list.append(duration // divisor_list[divisor_id])
    duration = duration % divisor_list[divisor_id]
for unit_id in range(len(unit_list)):
    if result_list[unit_id] == 0:
        continue
    result_string = result_string + str(result_list[unit_id]) + unit_list[unit_id]
print(result_string)