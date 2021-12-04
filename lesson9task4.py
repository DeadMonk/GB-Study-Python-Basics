# -*- coding: utf-8 -*-
# !/usr/bin/python3


from random import randint

class Car:
    def __init__(self, car_color, car_name):
        self.speed = 0
        self.color = car_color
        self.name = car_name
        self.is_police = 'police' in self.__class__.__name__.lower()

    def go(self):
        self.speed = randint(1, 180)
        return f'Автомобиль {self.name} двигается. Скорость {self.speed}.'

    def stop(self):
        self.speed = 0
        return f'Автомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'Автомобиль {self.name} выполнил поворот. Направление {direction}.'

    def show_speed(self):
        return self.speed

class PoliceCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости. {self.speed}'
        else:
            super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        return f'Превышение скорости. {self.speed}' if self.speed > 40 else self.speed

class SportCar(Car):
    pass

car1 = PoliceCar('blue', 'patrol')
print(car1.is_police)
print(car1.go())
print(car1.show_speed())
print(car1.turn('Север'))
print(car1.stop())

car2 = WorkCar('orange', 'watering machine')
print(car2.is_police)
print(car2.go())
print(car2.show_speed())
print(car2.turn('Право'))
print(car2.stop())
