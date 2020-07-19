# task 1
"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def div(*args):

    try:
        arg1 = float(input('Введите числитель: '))
        arg2 = float(input('Веведите знаменатель: '))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Ошибка! Делить на 0 нельзя."

    return res

print(f'Результат: {div()}')
