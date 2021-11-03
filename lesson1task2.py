# -*- coding: utf-8 -*-
#!/usr/bin/python3

# Создание списка
cube_list = []
for base_degree in range(1, 1000, 2):
    cube_list.append(base_degree ** 3)
print(cube_list)

# Вычисление суммы пункт a.
amount = 0
for cube in cube_list:
    digit_amount = 0
    number = cube
    while number > 0:
        digit = number % 10
        digit_amount += digit
        number = number // 10
    if digit_amount % 7 == 0:
        amount += cube
print(amount)

# Вычисление суммы пункт b. (В задании указано "К каждому элементу списка добавить 17".)
# Ниже представленно решение задачи исходя из предполжения, что добавить - операция сложения.
amount = 0
for cube in cube_list:
    digit_amount = 0
    number = cube + 17
    while number > 0:
        digit = number % 10
        digit_amount += digit
        number = number // 10
    if digit_amount % 7 == 0:
        amount += cube + 17
print(amount)
# Ниже представленно решение задачи исходя из предполжения, что добавить - операция конкатенации.
amount = 0
for cube in cube_list:
    digit_amount = 0
    number = cube
    while number > 0:
        digit = number % 10
        digit_amount += digit
        number = number // 10
    if (digit_amount + 8) % 7 == 0:
        amount += cube * 100 + 17
print(amount)