# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


class MainExceptioin(Exception):
    pass


class IamGodError(MainExceptioin):
    pass


class DrunkError(MainExceptioin):
    pass


class CarCrashError(MainExceptioin):
    pass


class GluttonyError(MainExceptioin):
    pass


class DepressionError(MainExceptioin):
    pass


class SuicideError(MainExceptioin):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0
day = 1


def one_day(_carma):
    _dice = randint(1, 13)
    raises = [
        IamGodError('был Богом'),
        DrunkError('напился'),
        CarCrashError('разбился на машине'),
        GluttonyError('обожрался'),
        DepressionError('был в депрессии'),
        SuicideError('покончил жизнь самоубийтсвом'),
    ]
    if _dice < 8:
        _carma += _dice
    else:
        raise raises[_dice-8]
    return _carma


with open('02_groundhog_day.log', 'a', encoding='UTF8') as file:
    while carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            carma = one_day(_carma=carma)
        except MainExceptioin as exc:
            file.write(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})\n')
        finally:
            day += 1
print(f'Достиг просветления за {day-1} дней')

# https://goo.gl/JnsDqu

# Зачёт!
