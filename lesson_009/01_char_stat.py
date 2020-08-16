# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import os
import zipfile
from collections import Counter


class Statistic:

    def __init__(self, _file_name, _sort_order, _sort_type):
        self.file_name = os.path.normpath(_file_name)
        self.stat = {}
        self.sort_stat = {}
        self.sort_order = _sort_order
        self.sort_type = _sort_type

    def run(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.collect()
        self.refactor_stat()
        print(self)

    def unzip(self):
        _filename = []
        with zipfile.ZipFile(self.file_name, 'r') as _zip_file:
            for _filename in _zip_file.namelist():
                _zip_file.extract(_filename)
        self.file_name = _filename

    def collect(self):
        _cnt = Counter('')
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                _str = "".join(x for x in line if x.isalpha())
                _cnt += Counter(_str)
        # TODO Преобразование в dict можно и делать. Counter явлеятся
        #  наследником класса dict
        self.stat = dict(_cnt)

    def refactor_stat(self):
        self.sort_stat = {}
        _eng_rus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                   'abcdefghijklmnopqrstuvwxyz' \
                   'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
                   'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        if self.sort_type == 'value':
            # TODO Попробуйте упростить выражение, преобразуя результат возвращаемый из sorted
            #  обрато в словарь:
            #  self.sort_stat = dict(sorted(self.stat.items(), key=operator.itemgetter(1), reverse=...)
            self.sort_stat = {item: self.stat[item] for item in
                              sorted(self.stat, key=self.stat.__getitem__, reverse=self.sort_order)}
        else:
            # TODO Будет немного оптимальней в зависимости от условия развернуть
            #  строку с буквами, а вызов dict.fromkeys оставить один.
            if self.sort_order:
                self.sort_stat = dict.fromkeys(reversed(_eng_rus))
            else:
                self.sort_stat = dict.fromkeys(_eng_rus)
            self.sort_stat.update(self.stat)

    def __str__(self):
        _total = 0
        print('+---------+----------+\n|  буква  | частота  |\n+---------+----------+')
        for item in self.sort_stat.items():
            if item[1] is not None:
                print(f'|{item[0]:^9}|{item[1]:>8d}  |')
                _total += item[1]
        print('+---------+----------+')
        return f'|  ИТОГО  |{_total:^10d}|\n+---------+----------+'


new_stat = Statistic(_file_name='python_snippets/voyna-i-mir.txt.zip', _sort_order=True, _sort_type='value')
text = ' по частоте по убыванию '
print(f'{text:#^30}')
new_stat.run()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
text = ' по частоте по возрастанию '
print(f'{text:#^30}')
new_stat.sort_order = False
new_stat.run()
text = ' по алфавиту по возрастанию '
print(f'{text:#^30}')
new_stat.sort_type = 'key'
new_stat.run()
text = ' по алфавиту по убыванию '
print(f'{text:#^30}')
new_stat.sort_order = True
new_stat.run()
