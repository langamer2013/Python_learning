# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys

commands_to_write = []

filename = "config_sw1.txt"
with open(filename, 'r') as file:
    for line in file:
        if not line.startswith('!') and ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
            commands_to_write.append(line.rstrip())

with open('new_file', 'w') as dst:
    dst.write('\n'.join(commands_to_write))

