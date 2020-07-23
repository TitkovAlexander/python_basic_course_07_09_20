# task 1

"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, time, salary, premium = argv

try:
    time = int(time)
    salary = int(salary)
    premium = int(premium)
    res = time * salary + premium
    print(f'Заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
