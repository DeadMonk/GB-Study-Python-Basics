# -*- coding: utf-8 -*-
# !/usr/bin/python3


def num_translate(numeral: str):
    numeral_dict = {'zero': 'ноль',
                    'one': 'один',
                    'two': 'два',
                    'three': 'три',
                    'four': 'четыре',
                    'five': 'пять',
                    'six': 'шесть',
                    'seven': 'семь',
                    'eight': 'восемь',
                    'nine': 'девять',
                    'ten': 'десять'}
    if numeral.istitle() and numeral.lower() in numeral_dict.keys():
        return numeral_dict.get(numeral.lower()).title()
    elif numeral.isupper() and numeral.lower() in numeral_dict.keys():
        return numeral_dict.get(numeral.lower()).upper()
    else:
        return numeral_dict.get(numeral.lower())