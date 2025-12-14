# -*- coding: utf-8 -*-
from pprint import pprint
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну
общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент
список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между
устройствами. Структура словаря такая же, как в задании 11.1:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.
Если функция parse_cdp_neighbors не может обработать вывод одного из файлов
с выводом команды, надо исправить код функции в задании 11.1.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

infiles2 = [
    "sh_cdp_n_sw1.txt"
]
def create_network_map(filenames):
    network_map = {}
    for file in filenames:
        with open(file, 'r') as f:
            for line in f:
                if '>' in line:
                    r_name = line.split('>')[0]
                if 'Eth' in line:
                    neig_device, _, local_int, *_, neig_int = line.split()
                    network_map[(r_name, f'Eth{local_int}')] = (neig_device, f'Eth{neig_int}')
    return network_map

pprint(create_network_map(infiles))

def uniq_net_map(net_map):
    uniq_map = {}
    for line_key, line_value in net_map.items():
        if not uniq_map.get(line_key) and not (uniq_map.get(line_value) == line_key):
            uniq_map[line_key] = line_value
            #pprint(uniq_map)
    return uniq_map

print('=' * 50)

pprint(uniq_net_map(create_network_map(infiles)))


"""
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
 ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}
 """