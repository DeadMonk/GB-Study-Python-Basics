# -*- coding: utf-8 -*-
# !/usr/bin/python3


result_list = []
with open('nginx_logs', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        tmp_list = log_file.readline().replace('"', '').split()
        result_list.append((tmp_list[0], tmp_list[5], tmp_list[6]))

result_dict = {}
with open('nginx_logs', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        client_ip = log_file.readline().split()[0]
        result_dict.setdefault(client_ip, 0)
        result_dict[client_ip] += 1

print(sorted(result_dict.items(), key=lambda item: item[1], reverse=True)[0])
