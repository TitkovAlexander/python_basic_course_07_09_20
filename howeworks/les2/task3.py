# task 3
"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

while True:
    month = input('Введите месяц в виде целого числа от 1 до 12: ')
    if month.isdigit():
        month = int(month)
        break

    print('Ошибка ввода. Вы ввели не число.')


seasons = {
    'Зима': (1, 2, 12),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}

for key in seasons.keys():
    if month in seasons[key]:
        print(key)


if (month == 1 or month == 2 or month == 12):
    print('Зима')
elif (month == 3 or month == 4 or month == 5):
    print('Весна')
elif (month == 6 or month == 7 or month == 8):
    print('Лето')
elif (month == 9 or month == 10 or month == 11):
    print('Осень')
