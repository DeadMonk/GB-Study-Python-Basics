# -*- coding: utf-8 -*-
# !/usr/bin/python3


import re
import requests


RE_LPE = re.compile(r'((?:\d{1,3}\.){3}\d{1,3})[ -]+\[(.+)\]\s\"([A-Z]{3,6})\s(\/\S+)\s\S+\"\s(\d+)\s(\d+)')

log = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

print(RE_LPE.findall(log))

