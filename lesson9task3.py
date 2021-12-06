# -*- coding: utf-8 -*-
# !/usr/bin/python3


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())

employee1 = Position('Владимир', 'Иванов', 'токарь', 80000, 20000)

print(employee1.get_total_income())
print(employee1.get_full_name())

