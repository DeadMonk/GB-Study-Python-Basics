# -*- coding: utf-8 -*-
# !/usr/bin/python3


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([num for i, num in enumerate(src[1:]) if num > src[i]])

