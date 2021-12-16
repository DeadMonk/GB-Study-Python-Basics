# -*- coding: utf-8 -*-
#!/usr/bin/python3


from random import sample

class Game:
    def __init__(self):
        self.__rounds = sample(range(1, 91), 90)

    def round(self):
        for n in self.__rounds:
            print(n)

class NotInTicket(Exception):
    def __init__(self, txt):
        self.txt = txt

class Ticket:
    def __init__(self):
        self.numbers = sample(range(1, 91), 15)
        self.crossout = []

    def __str__(self):
        result = ''
        for k in range(0, 14, 5):
            for number in sorted(self.numbers[k:k+5]):
                if number in self.crossout:
                    result += '- '
                else:
                    result += f'{number} '
            result += '\n'
        return result

    def __sub__(self, other):
        if other in self.numbers:
            self.crossout.append(other)
        else:
            raise NotInTicket('Нет такого числа в карточке!')

    @property
    def strikethrough(self):
        return len(self.numbers) == len(self.crossout)












"""
На момент 14.12.2021 не смог закончить в связи с болезнью. Пока не получается реализовать код в ООП парадигме.

    Объекты:
            Билет
            Игрок
            Игра


1. получаем билет
2. объявляется номер из кубышки
3. смотрим

"""


# for k, i in enumerate(sample(range(1, 91), 90), start=1, ):
#     print(k, i)


k1 = Ticket()
print(k1.strikethrough)