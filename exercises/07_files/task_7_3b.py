# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan=input("Номер влан:")
macs=[]
with open('CAM_table.txt', 'r') as file:
    for line in file:
        if 'DYNAMIC' in line:
            line=line.rstrip().split()
            macs.append(line)

for i in macs:
    i[0]=int(i[0])

for i in sorted(macs):
    if vlan == str(i[0]):
        print(i[0], i[1], i[3])

