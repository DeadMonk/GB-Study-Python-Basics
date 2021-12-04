# -*- coding: utf-8 -*-
# !/usr/bin/python3


class Road:
    def __init__(self, road_length, road_width):
        self._length = road_length
        self._width = road_width

    def road_mass(self):
        return self._length * self._width * 5 * 25

m6 = Road(1381000, 7)

print(m6.road_mass())


