# task 3

"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

import random

random_list = [random.randint(0, 100) for i in range(3)]
print(random_list)

def my_func():
    list = random_list
    total = []
    max_1 = max(list)
    total.append(max_1)
    list.remove(max_1)
    max_2 = max(list)
    total.append(max_2)
    print(sum(total))

my_func()