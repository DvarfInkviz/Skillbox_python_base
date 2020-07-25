# -*- coding: utf-8 -*-

from random import sample

_secret_number = ''


# TODO Не самый оптимальный способ генерации числа.
#  В библиотеке random есть более подходящие функции.
#  Например shuffle или sample. С sample можно получить
#  сразу всю случайную последовательность одной командой.
#  Если хотите избегать 0 на первой позиции,
#  то генерировать последовательлность можно в цикле,
#  пока не получится последовательность начинающуася не с 0.
#  Или можно вместо последовательности в 4 символа сгенерировать 5
#  И если на первой позиции 0 сделать срез списка [1:], если не 0 [:4]
#  Функция shuffle позволяет перемешать элементы списка,
#  который можно сделать как list(range(10)). Останется только проверить
#  0 элемент и использовать срез.
def guess_number():
    global _secret_number
    numbers = '0123456789'
    while True:
        num = sample(numbers, 4)
        _secret_number = ''.join([str(item) for item in num])
        if _secret_number[0] != 0:
            break
    print(_secret_number)


def check_number(estimated_number):
    res = {'bulls': 0, 'cows': 0}
    for i, number in enumerate(estimated_number):
        print(i, number, estimated_number)
        if _secret_number.index(number) == i:
            res['bulls'] += 1
        elif number in _secret_number:
            res['cows'] += 1
    return res
