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

import zipfile


class Statistic:

    def __init__(self, _file_name, _sort_order, _sort_type):
        self.file_name = _file_name
        self.stat = {}
        self.sort_stat = {}
        self.sort_order = _sort_order
        self.sort_type = _sort_type

    def run(self):
        # self.__init__(self.file_name, self.sort_order, self.sort_type)
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.collect()
        if self.sort_type == 'key':
            self.refactor_stat()
        print(self)

    def unzip(self):
        _filename = []
        _zip_file = zipfile.ZipFile(self.file_name, 'r')
        for _filename in _zip_file.namelist():
            _zip_file.extract(_filename)
        self.file_name = _filename

    def collect(self):
        self.stat = {}
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for i, line in enumerate(file):
                self._collect_for_line(line=line[:-1])
                # print(self.stat)
                if i == 100:
                    break

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def refactor_stat(self):
        self.sort_stat = {}
        if self.sort_type == 'key':
            self.sort_stat = {k: self.stat[k] for k in sorted(self.stat, key=self.stat.get, reverse=self.sort_order)}

    def __str__(self):
        _total = 0
        if self.sort_type == 'key':
            for item in self.sort_stat.items():
                print(f'|{item[0]:^7}|{item[1]:^10d}|')
                _total += item[1]
        elif not self.sort_order:
            for item in reversed(sorted(self.stat.items())):
                print(f'|{item[0]:^7}|{item[1]:^10d}|')
                _total += item[1]
        else:
            for item in sorted(self.stat.items()):
                print(f'|{item[0]:^7}|{item[1]:^10d}|')
                _total += item[1]
        return f'ИТОГО : {_total}'


new_stat = Statistic(_file_name='python_snippets\\voyna-i-mir.txt.zip', _sort_order=True, _sort_type='key')
text = ' по частоте по убыванию '
print(f'{text:#^50}')
new_stat.run()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
text = ' по частоте по возрастанию '
print(f'{text:#^50}')
new_stat.sort_order = False
new_stat.run()
text = ' по алфавиту по возрастанию '
print(f'{text:#^50}')
new_stat.sort_order = True
new_stat.sort_type = 'value'
new_stat.run()
text = ' по алфавиту по убыванию '
print(f'{text:#^50}')
new_stat.sort_order = False
new_stat.run()