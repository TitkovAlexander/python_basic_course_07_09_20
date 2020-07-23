# task 2
""" Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random

random_list = [random.randint(0, 100) for i in range(10)]
print(random_list)

my_list = [el for num, el in enumerate(random_list) if random_list[num - 1] < random_list[num]]
print(my_list)