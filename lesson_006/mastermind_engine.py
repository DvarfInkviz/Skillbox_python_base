# -*- coding: utf-8 -*-

from random import sample

_secret_number = ''


def guess_number():
    global _secret_number
    numbers = '0123456789'
    while True:
        num = sample(numbers, 4)
        if num[0] != '0':
            _secret_number = ''.join([str(item) for item in num])
            break


def check_number(estimated_number):
    res = {'bulls': 0, 'cows': 0}
    for i, _number in enumerate(estimated_number):
        if _secret_number[i] == _number:
            res['bulls'] += 1
        elif _number in _secret_number:
            res['cows'] += 1
    return res
