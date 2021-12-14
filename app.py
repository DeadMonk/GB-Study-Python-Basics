# -*- coding: utf-8 -*-
#!/usr/bin/python3


from random import sample
#
# class Ticket:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#
# class Player:


"""
На момент 14.12.2021 не смог закончить в связи с болезнью. Пока не получается реализовать код в ООП парадигме.

    Объекты:
            Билет
            Игрок
            Кубышки
            Игра


1. получаем билет
2. объявляется номер из кубышки
3. смотрим

"""

# class Ticket:
#     def __init__(self):
#
#
#
#
#
# class Tub:
#     def newone(self):
#         return randint(1, 90)

bn = []
k = sample(range(1, 91), 15)
print(type(k))
bn = [sorted(sample(range(0, 9), 5)) for _ in range(3)]
print(bn)

for i, el in enumerate(k, start=1):
    if not i % 5:
        print(el)
    else:
        print(el, end=' ')