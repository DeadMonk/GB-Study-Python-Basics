# -*- coding: utf-8 -*-
#!/usr/bin/python3


class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def __add__(self, other):
        self.cell_num += other.cell_num
        return self

    def __sub__(self, other):
        if self.cell_num < other.cell_num:
            raise Exception('Клетка с отрицательным количеством ячеек.')
        else:
            self.cell_num -= other.cell_num
            return self

    def __mul__(self, other):
        self.cell_num *= other.cell_num
        return self

    def __floordiv__(self, other):
        self.cell_num //= other.cell_num
        return self

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def __str__(self):
        return str(f'Клетка из {self.cell_num} ячеек')

    def make_order(self, row):
        result = ''
        for _ in range(self.cell_num // row):
            result += ('*' * row + '\n')
        result += ('*' * (self.cell_num % row) + '\n')
        return result
