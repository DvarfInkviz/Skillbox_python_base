# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def _parse_line(_line):
    _data = _line.split(' ')
    if len(_line) == 0 or _line.isspace():
        raise ValueError('НЕ присутсвуют все три поля!')
    elif len(_data) == 3:
        if not _data[0].isalpha():
            raise NotNameError('поле имени содержит НЕ только буквы!')
        if '@' not in _data[1] or '.' not in _data[1]:
            raise NotEmailError('поле емейл НЕ содержит @ и/или .(точку)')
        if _data[2].isalnum():
            if not 10 <= int(_data[2]) <= 99:
                raise ValueError('поле возраст НЕ является числом от 10 до 99!')
        else:
            raise ValueError('поле возраст НЕ является числом!')
    else:
        raise IndexError('Не все поля заполнены!')


class LogParser:

    def __init__(self, _log_file):
        self.log_file = os.path.normpath(_log_file)
        self.good_log = 'registrations_good.log'
        self.bad_log = 'registrations_bad.log'

    def run(self):
        self.parse_file()
        print('All Done!')

    def parse_file(self):
        with open(self.log_file, 'r', encoding='UTF8') as _file, open(self.bad_log, 'a', encoding='UTF8') as _bad_file,\
                open(self.good_log, 'a', encoding='UTF8') as _good_file:
            for line in _file:
                try:
                    _parse_line(_line=line[:-1])
                except ValueError as exc:
                    _bad_file.write(f'{line[:-1]:<50} - ERROR: {exc.args[0]}\n')
                except NotNameError as exc:
                    _bad_file.write(f'{line[:-1]:<50} - ERROR: {exc.args[0]}\n')
                except NotEmailError as exc:
                    _bad_file.write(f'{line[:-1]:<50} - ERROR: {exc.args[0]}\n')
                except IndexError as exc:
                    _bad_file.write(f'{line[:-1]:<50} - ERROR: {exc.args[0]}\n')
                else:
                    _good_file.write(line)


log = LogParser(_log_file='registrations.txt')
log.run()

# Зачёт!
