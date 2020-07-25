# -*- coding: utf-8 -*-

from random import randint

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
    numbers = list('0123456789')
    _secret_number = numbers.pop(randint(1, 9))
    _secret_number += numbers.pop(randint(0, 8))
    _secret_number += numbers.pop(randint(0, 7))
    _secret_number += numbers.pop(randint(0, 6))
    print(_secret_number)


def check_number(estimated_number):
    res = {'bulls': 0, 'cows': 0}
    for i, number in enumerate(estimated_number):
        # TODO Если поменять местами условия и сначала искать быков,
        #  а второй проверкой в elif с оператором in искать коров
        #  то код станет немного компактней.
        if number in _secret_number:
            if _secret_number.index(number) == i:
                res['bulls'] += 1
            else:
                res['cows'] += 1
    return res
