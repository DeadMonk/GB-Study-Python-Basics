# -*- coding: utf-8 -*-
# !/usr/bin/python3


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_klasses = ((tutors[i], klasses[i]) if i <= len(klasses) - 1 else (tutors[i], None) for i in range(len(tutors)))

print(type(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
