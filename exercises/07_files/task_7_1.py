# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open('ospf.txt')
format_template ="""
Prefix                {0:<8}
AD/Metric             {1:<8}
Next-Hop              {2:<8}
Last update           {3:<8}
Outbound Interface    {4:<8}
"""

for line in f:
    prefix = line.split()[1]
    metric = line.split()[2].replace('[', '').replace(']', '')
    next_hop = line.split()[4].replace(',', '')
    last_update = line.split()[5].replace(',', '')
    out_int = line.split()[6]
    print(format_template.format(prefix, metric, next_hop, last_update, out_int))

