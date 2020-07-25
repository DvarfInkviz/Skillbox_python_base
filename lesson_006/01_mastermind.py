# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


from mastermind_engine import guess_number, check_number
# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT
from termcolor import colored


def is_number_correct(_number):
    numbers = '0123456789'
    if _number.isdigit():
        # TODO Для проверки числа на уникальность цифр можно преобразовать строку в множество.
        #  Если длина множества будет равна длине строки, значит строка состоит из уникальных символов.
        if len(_number) == 4:
            if _number[0] in numbers[1:]:
                numbers = numbers.replace(_number[0], '')
                if _number[1] in numbers:
                    numbers = numbers.replace(_number[1], '')
                    if _number[2] in numbers:
                        numbers = numbers.replace(_number[2], '')
                        if _number[3] in numbers:
                            return True
    return False


iteration = 0
guess_number()
print('Загаданное число пока нам неизвестно )')
number = input(colored('Введите число ', color='blue'))
while True:
    iteration += 1
    if is_number_correct(number):
        answer = check_number(number)
        print(f"Быков - {answer['bulls']}; коров - {answer['cows']}")
        if answer['bulls'] == 4:
            new_game = input(colored(f'Вы отгадали число! Затрачено {iteration} хода(ов)!\nХотите еще партию? (y/n) ',
                                     color='magenta'))
            while True:
                if (new_game == 'y') or (new_game == 'Y'):
                    iteration = 0
                    guess_number()
                    print('Загаданное число пока нам неизвестно )')
                    number = input(colored('Введите число ', color='blue'))
                    break
                elif (new_game == 'n') or (new_game == 'N'):
                    break
                else:
                    new_game = input(colored('Что-то неразборчиво! Хотите еще партию? (y/n) ', color='red'))
            if (new_game == 'y') or (new_game == 'Y'):
                continue
            else:
                break
        else:
            number = input(colored('Попробуйте еще раз: ', color='blue'))
    else:
        number = input(colored('Введи число в правильном формате: ', color='red'))

# TODO Исправьте замечания в модуле mastermind_engine
