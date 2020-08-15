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


# TODO Для исключений, созданных в этом задании лучше сделать общий родительский класс,
#  например MainException, унаследованный от Exception, от которого нужно
#  наследовать остальные а в except перехватывать общее исключение MainException.
class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0
day = 1


def write_log(_message):
    with open('02_groundhog_day.log', 'a', encoding='UTF8') as file:
        file.write(f'{_message}\n')


def one_day(_carma):
    _dice = randint(1, 13)
    if _dice < 8:
        _carma += _dice

    # TODO Можно упростить код с условиями:
    #  Перечислить исключения в списке или кортеже, случайно выбирать один
    #  из элементов списка и вызывать полученное исключение.
    elif _dice == 8:
        raise IamGodError('был Богом')
    elif _dice == 9:
        raise DrunkError('напился')
    elif _dice == 10:
        raise CarCrashError('разбился на машине')
    elif _dice == 11:
        raise GluttonyError('обожрался')
    elif _dice == 12:
        raise DepressionError('был в депрессии')
    elif _dice == 13:
        raise SuicideError('покнчил жизнь самоубийтсвом')
    return _carma


while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        carma = one_day(_carma=carma)
    # TODO Если сделать общий класс для всех ошибок, то в следующей строке
    #  можно будет перехватывать только одно общее исключение.
    except IamGodError as exc:
        write_log(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})')
    except DrunkError as exc:
        write_log(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})')
    except CarCrashError as exc:
        write_log(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})')
    except GluttonyError as exc:
        write_log(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})')
    except DepressionError as exc:
        write_log(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})')
    except SuicideError as exc:
        write_log(f'Необычный {day} день! Он {exc.args[0]} (Карма ={carma})')
    finally:
        day += 1
print(f'Достиг просветления за {day-1} дней')

# https://goo.gl/JnsDqu
