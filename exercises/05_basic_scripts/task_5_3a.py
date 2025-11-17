# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

input_int_type = input("Введите режим работы интерфейса (access/trunk):")
input_int_num = input("Введите тип и номер интерфейса:")
int_type_for_vlan={}
int_type_for_vlan.update({'trunk': 'Введите разрешенные VLANы:', 'access': 'Введите номер VLAN:'})
input_vlans = input(int_type_for_vlan[input_int_type])
#input_vlans = input("Введите номер влан(ов):")

int_type_dict={}
int_type_dict.update({'trunk': trunk_template, 'access': access_template})
print(f"interface {input_int_num}")
cur_temp='\n'.join(int_type_dict[input_int_type])

print('\n'.join(int_type_dict[input_int_type]).format(input_vlans))