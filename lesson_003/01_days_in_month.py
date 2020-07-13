# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
while True:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    if user_input.isdigit():
        month = int(user_input)
        if 0 < month <= 12:
            print('Вы ввели', month)
            break
        else:
            print('Вы ввели некорректный номер месяца!')
    else:
        print('Вы ввели некорректный номер месяца!')

if month == 2:
    user_input = '02'

days_in_month = {
    '28': '02',
    '30': '46911',
    '31': '135781012',
}

for days, months in days_in_month.items():
    if user_input in months:
        print(days)
        break

