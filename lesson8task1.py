# -*- coding: utf-8 -*-
# !/usr/bin/python3


import re

RE_EMAIL = re.compile(r'([-_.a-z\d]+)@([-_.a-z\d]+\.[a-z\d]+)')

def email_parser(mail: str):
    if RE_EMAIL.match(mail):
        name, domain = RE_EMAIL.findall(mail)[0]
        return {'username': name, 'domain': domain }
    else:
        raise ValueError(f'Wrong email: {mail}')


