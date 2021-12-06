# -*- coding: utf-8 -*-
# !/usr/bin/python3


from time import sleep


class TrafficLight:
    __color = {'red': 7, 'yelow': 2, 'green': 6}

    def running(self):
        while True:
            for color, timer in self.__color.items():
                print(color)
                sleep(timer)


k1 = TrafficLight()

k1.running()
