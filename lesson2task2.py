# -*- coding: utf-8 -*-
#!/usr/bin/python3

# '05'.isdigit() == True
# '5'.zfill(2) == 05

base_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result_string = ''
encounter = 0
encounter_list = []
while encounter < len(base_list):
    if base_list[encounter].isdigit():
        base_list[encounter] = base_list[encounter].zfill(2)
        base_list.insert(encounter, '"')
        base_list.insert(encounter + 2, '"')
        encounter_list.append(encounter)
        encounter += 3
    else:
        start_digit = None
        for symbol_id, symbol in enumerate(base_list[encounter]):
            if symbol.isdigit():
                start_digit = symbol_id
        if start_digit != None:
            have_digit = base_list[encounter]
            base_list[encounter] = f'{have_digit[:start_digit]}{have_digit[start_digit:].zfill(2)}'
            base_list.insert(encounter, '"')
            base_list.insert(encounter + 2, '"')
            encounter_list.append(encounter)
            encounter += 3
        else:
            encounter += 1
start_id = 0
for quote in encounter_list:
    result_string += f"{' '.join(base_list[start_id:quote])} {''.join(base_list[quote:quote+3])} "
    start_id = quote + 3
if encounter_list[-1] + 2 < len(base_list) - 1:
    result_string += f"{' '.join(base_list[encounter_list[-1] + 3:])}"
print(base_list)
print(result_string)