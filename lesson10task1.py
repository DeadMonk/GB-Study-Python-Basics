# -*- coding: utf-8 -*-
#!/usr/bin/python3


class Matrix:
    def __init__(self, input_list):
        self.matrix = input_list

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in  self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise Exception('Матрицы имеют разные размерности')
        else:
            for l1, l2 in zip(self.matrix, other.matrix):
                line = [ for el1, el2]



m1 = Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1)))

print(m1)