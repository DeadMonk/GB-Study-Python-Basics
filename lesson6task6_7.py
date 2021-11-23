# -*- coding: utf-8 -*-
# !/usr/bin/python3


def get_end(file_name: str):
    with open(file_name, 'a', encoding='utf-8') as dfile:
        return dfile.tell()


def index_lines(file_name: str):
    line_index = {1: 0}
    with open(file_name, 'r', encoding='utf-8') as dfile:
        line_id = 2
        while dfile.tell() != get_end(file_name):
            dfile.readline()
            line_index.update({line_id: dfile.tell()})
            line_id += 1
    return line_index


def add_record(file_name: str, rec_data: str):
    with open(file_name, 'a', encoding='utf-8') as dfile:
        print(rec_data, file=dfile)


def read_record(file_name: str, rnum=None):
    fidx = index_lines(file_name)
    if get_end(file_name) == 0:
        return 'Empty File'
    if fidx.get(rnum) is not None:
        with open(file_name, 'r', encoding='utf-8') as dfile:
            dfile.seek(fidx[rnum])
            return dfile.readline()
    else:
        with open(file_name, 'r', encoding='utf-8') as dfile:
            dfile.seek(fidx[[*fidx.keys()][-2]])
            return dfile.readline()


def read_records(file_name: str, rnum_start: int, rnum_end=None):
    fidx = index_lines(file_name)
    if fidx.get(rnum_start) is None:
        return 'Wrong line number'
    if not rnum_end or not fidx.get(rnum_end) or rnum_start > rnum_end:
        rnum_end = [*fidx.keys()][-1]
    hint = fidx[rnum_end] - fidx[rnum_start]
    with open(file_name, 'r', encoding='utf-8') as dfile:
        dfile.seek(fidx.get(rnum_start))
        return dfile.readlines(hint)


def edit_record(file_name: str, rnum: int, new_value: str):
    fidx = index_lines(file_name)
    if not fidx.get(rnum):
        add_record(file_name, new_value)
    else:
        with open(file_name, 'r+', 1, encoding='utf-8') as dfile:
            buff_data = bytearray()
            dfile.buffer.seek(fidx[rnum + 1] - 1)
            for data in dfile.buffer.readlines():
                buff_data.extend(data)
            dfile.buffer.seek(fidx[rnum])
            dfile.buffer.truncate(fidx[rnum])
            dfile.buffer.write(new_value.encode('utf8'))
            dfile.buffer.write(buff_data)


