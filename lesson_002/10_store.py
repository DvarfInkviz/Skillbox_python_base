#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

table_code = goods['Стол']
table_item = store[table_code][0]
table_quantity = table_item['quantity']
table_price = table_item['price']
table_cost = table_quantity * table_price
table_item = store[table_code][1]
table_quantity += table_item['quantity']
table_price = table_item['price']
table_cost += table_item['quantity'] * table_price
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

# table_qnt = store[goods['Стол']][0]['quantity']
# table_cost = table_qnt * store[goods['Стол']][0]['price']
# table_qnt += store[goods['Стол']][1]['quantity']
# table_cost += store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
# print('Стол -', table_qnt, 'шт, стоимость', table_cost, 'руб')

sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost = sofa_quantity * sofa_price
sofa_item = store[sofa_code][1]
sofa_quantity += sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost += sofa_item['quantity'] * sofa_price
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

# sofa_qnt = store[goods['Диван']][0]['quantity']
# sofa_cost = sofa_qnt * store[goods['Диван']][0]['price']
# sofa_qnt += store[goods['Диван']][1]['quantity']
# sofa_cost += store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
# print('Диван -', sofa_qnt, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_quantity * chair_price
chair_item = store[chair_code][1]
chair_quantity += chair_item['quantity']
chair_price = chair_item['price']
chair_cost += chair_item['quantity'] * chair_price
chair_item = store[chair_code][2]
chair_quantity += chair_item['quantity']
chair_price = chair_item['price']
chair_cost += chair_item['quantity'] * chair_price
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')

# chair_qnt = store[goods['Стул']][0]['quantity']
# chair_cost = chair_qnt * store[goods['Стул']][0]['price']
# chair_qnt += store[goods['Стул']][1]['quantity']
# chair_qnt += store[goods['Стул']][2]['quantity']
# chair_cost += store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
# chair_cost += store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
# print('Стул -', chair_qnt, 'шт, стоимость', chair_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

# Зачёт!
