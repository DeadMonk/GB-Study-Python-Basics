# -*- coding: utf-8 -*-
# !/usr/bin/python3


from requests import get
from datetime import date

def pars_field(fields: str, field_name: str):
    return fields[fields.find(f'<{field_name}>')+ len(f'<{field_name}>'):fields.find(f'</{field_name}>')]

def pars_date(fields: str):
    date_list = fields[fields.find('Date="') + len('Date="'): fields.find('" name="')].split('.')
    return date(day=int(date_list[0]), month=int(date_list[1]), year=int(date_list[2]))

def currency_rates(cccode='all', cdate=True):
    erdata = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    cdata = erdata[erdata.find('<Valute ID'): erdata.rfind('</Valute>') + len('</Valute>')]
    cdict = {}
    if cdate:
        cdict.update({'date': pars_date(erdata)})
    for currency in cdata.split('</Valute>'):
        if len(currency) == 0:
            break
        cur_id = currency[currency.find('ID="') + len('ID="'): currency.find('><')]
        num_code = pars_field(currency, 'NumCode')
        char_code = pars_field(currency, 'CharCode')
        nominal = int(pars_field(currency, 'Nominal'))
        name = pars_field(currency, 'Name')
        value = float(pars_field(currency, 'Value').replace(',','.'))
        cdict.update({char_code: {'name': name, 'id': cur_id, 'num_code': num_code, 'nominal': nominal, 'value': value}})
    if cccode == 'all':
        return cdict
    else:
        return pars_date(erdata), cdict.get(cccode)


