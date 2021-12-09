# -*- coding: utf-8 -*-
#!/usr/bin/python3


from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def outgo(self):
        pass

class Coat(Clothes):
    @property
    def outgo(self):
        return self.value / 6.5 + 0.5

class Suit(Clothes):
    @property
    def outgo(self):
        return 2 * self.value + 0.3


