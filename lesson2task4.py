# -*- coding: utf-8 -*-
#!/usr/bin/python3

base_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']


for employee in base_list:
    print(f'Привет, {employee.split()[-1].title()}!')


for employee in base_list:
    print(f'Привет, {employee[employee.rfind(" ") + 1:].title()}!')



