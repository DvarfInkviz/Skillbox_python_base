# -*- coding: utf-8 -*-

# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint

_secret_number = ''


def guess_number():
    global _secret_number
    numbers = list('0123456789')
    _secret_number = numbers.pop(randint(1, 9))
    _secret_number += numbers.pop(randint(0, 8))
    _secret_number += numbers.pop(randint(0, 7))
    _secret_number += numbers.pop(randint(0, 6))
    print(_secret_number)


def check_number(estimated_number):
    res = {'bulls': 0, 'cows': 0}
    for i, number in enumerate(estimated_number):
        if number in _secret_number:
            if _secret_number.index(number) == i:
                res['bulls'] += 1
            else:
                res['cows'] += 1
    return res
