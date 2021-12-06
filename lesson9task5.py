# -*- coding: utf-8 -*-
# !/usr/bin/python3


class Stationery:
    def __init__(self):
        self.title = self.__class__.__name__
    def draw(self):
        return 'Запуск отрисовки.'

class Pen(Stationery):
    def draw(self):
        return 'Пишем ручкой.'

class Pencil(Stationery):
    def draw(self):
        return 'Чертим карандашом.'

class Handle(Stationery):
    def draw(self):
        return 'Отмечаем маркером.'



drawing = Stationery()
bic = Pen()
koh_i_noor = Pencil()
touch_cool = Handle()

print(drawing.title, drawing.draw())
print(bic.title, bic.draw())
print(koh_i_noor.title, koh_i_noor.draw())
print(touch_cool.title, touch_cool.draw())