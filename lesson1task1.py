# -*- coding: utf-8 -*-
#!/usr/bin/python3

duration = input('Введите количество секунд: ')

duration = int(duration)

if duration >= 86400:
    print(duration // 86400, 'дн', (duration % 86400) // 3600, 'час', ((duration % 86400) % 3600) // 60, 'мин', duration % 60, 'сек')
elif duration >= 3600:
    print(duration // 3600, 'час', (duration % 3600) // 60, 'мин', (duration % 3600) % 60, 'сек')
elif duration >= 60:
    print(duration // 60, 'мин', duration % 60, 'сек')
else:
    print(duration, 'сек')

print(duration % 60, duration // 60 % 60, duration // 60 // 60, duration // 60 // 60 // 24)


divisor = [86400, 3600, 60]
