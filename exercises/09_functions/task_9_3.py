# -*- coding: utf-8 -*-
from pprint import pprint
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



#print(config)

def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as file:
        trunk = {}
        access = {}
        for line in file:
            if "FastEthernet" in line:
                portname = line.split()[1].strip()
            if "vlan" in line and "trunk" in line:
                trunk[portname] = line.split()[-1].strip().split(',')
                portname = ''
            elif "vlan" in line and "trunk" not in line:
                access[portname] = int(line.split()[-1].strip())
            elif "access" in line and "vlan" not in line:
                access[portname] = 1    
        return  access, trunk
        

pprint(get_int_vlan_map('config_sw2.txt'))