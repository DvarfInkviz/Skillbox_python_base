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
            print(_secret_number)
            break


def check_number(estimated_number):
    res = {'bulls': 0, 'cows': 0}
    for i, _number in enumerate(estimated_number):
        print(type(_number))
        print(i, _number, estimated_number)
        if _secret_number.index(_number) == i:
            res['bulls'] += 1
        elif _number in _secret_number:
            res['cows'] += 1
    return res
#  не могу никак понять почему выдается ошибка при проверке условия if _secret_number.index(_number) == i:
#  функции check_number. При попытке понять, что происходит, вписал print вокруг этого места
#  пример вывода в окне терминала с комментариями откуда ведется вывод:
# TODO Это стандартное исключение возникающее, когда при поиске индекса по значению элемента,
#  элемент в списке не найден.
#  Ошибку можно исправить, если в условии сравнивать _number с i-м значением _secret_number.

#  ---------------
#  F:\Python38\python.exe F:/SkillBox/Les01/lesson_006/01_mastermind.py
#   9214  ## line 15 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   Загаданное число пока нам неизвестно )  ## line 61 in File "F:/SkillBox/Les01/lesson_006/01_mastermind.py"
#   Введите число 1234  ## line 62 in File "F:/SkillBox/Les01/lesson_006/01_mastermind.py"
#   1234  ## line 65 in File "F:/SkillBox/Les01/lesson_006/01_mastermind.py"
#   Traceback (most recent call last):
#    File "F:/SkillBox/Les01/lesson_006/01_mastermind.py", line 68, in <module>
#      answer = check_number(number)
#    File "F:\SkillBox\Les01\lesson_006\mastermind_engine.py", line 24, in check_number
#      if _secret_number.index(_number) == i:
#   ValueError: substring not found
#   <class 'str'>  ## line 67 in File "F:/SkillBox/Les01/lesson_006/01_mastermind.py"
#   <class 'str'>  ## line 22 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   0 1 1234       ## line 23 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   <class 'str'>  ## line 22 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   1 2 1234       ## line 23 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   <class 'str'>  ## line 22 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   2 3 1234       ## line 23 in File "F:/SkillBox/Les01/lesson_006/mastermind_engine.py"
#   Process finished with exit code 1
#  ----------------
