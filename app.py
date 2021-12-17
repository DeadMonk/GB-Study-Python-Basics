# -*- coding: utf-8 -*-
#!/usr/bin/python3


from random import sample

class Game:
    def __init__(self, ct, pt):
        self.__rounds = sample(range(1, 91), 90)
        self.player = pt
        self.computer = ct

    def run(self):
        for n in self.__rounds:
            print(f'Карточка игрока:\n{self.player}')
            print(f'Карточка компьютера:\n{self.computer}')
            print(f'Выпал номер {n}')
            self.compmove(n)
            self.usermove(n)
            if self.computer.strikethrough or self.player.strikethrough:
                print(f'Выйграл Игрок: {self.player.strikethrough}\nВыйграл Компьютер: {self.computer.strikethrough}')
                break

    def compmove(self, number):
        if self.computer.checknumber(number):
            self.computer -= number

    def usermove(self, number):
        ansver = input('Чтобы вычеркнуть число введите Y: ')
        if ansver == 'y' or ansver == 'Y':
            self.player -= number


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

    def __isub__(self, other):
        if other in self.numbers:
            self.crossout.append(other)
            return self
        else:
            raise NotInTicket('Нет такого числа в карточке! Вы проиграли.')

    # def __isub__(self, other):
    #     return self.__sub__(other)

    def checknumber(self, number):
        return number in self.numbers

    @property
    def strikethrough(self):
        return len(self.numbers) == len(self.crossout)


k1 = Ticket()
k2 = Ticket()
game = Game(k1, k2)
game.run()