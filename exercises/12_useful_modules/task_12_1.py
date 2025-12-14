# -*- coding: utf-8 -*-
import subprocess
from pprint import pprint
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_list = [
    '8.8.8.8',
    '8.8.4.4',
    '11.12.13.14'
]

def ping_ip_addresses(list_addr):
    ip_reach = []
    ip_unreach = []
    for ip in list_addr:
        command = f"ping {ip} -n 3"
        result = subprocess.run(command, stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            ip_reach.append(ip)
        else:
            ip_unreach.append(ip)
    return ip_reach, ip_unreach

pprint(ping_ip_addresses(ip_list))

