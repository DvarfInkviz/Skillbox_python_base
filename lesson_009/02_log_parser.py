# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import zipfile


class LogParser:

    def __init__(self, _log_file, _group_type, _event):
        self.log_file = _log_file
        self.event = _event
        if self.event != 'OK' and self.event != 'NOK':
            self.event = 'NOK'
        self.group_var = {
            'yy': [5, 'годам'],
            'mm': [8, 'месяцам'],
            'h': [14, 'часам'],
            'm': [17, 'минутам']
        }
        self.group_type = self.group_var.get(_group_type, [17, 'минутам'])
        print(f'Группировка событий {self.event} будет проходить по {self.group_type[1]}!')
        self.result_file = f'events_{self.event}_{_group_type}.txt'
        self.log = {}

    def run(self):
        if self.log_file.endswith('.zip'):
            self.unzip()
        self.parse_file()
        print('All Done!')

    def unzip(self):
        _filename = []
        with zipfile.ZipFile(self.log_file, 'r') as _zip_file:
            for _filename in _zip_file.namelist():
                _zip_file.extract(_filename)
        self.log_file = _filename

    def parse_file(self):
        with open(self.log_file, 'r', encoding='UTF8') as file:
            for line in file:
                self._parse_line(line=line[:-1])
        self._write_result()

    def _parse_line(self, line):
        if self.event in line:
            _date = line[:self.group_type[0]]
            if _date in self.log:
                self.log[_date] += 1
            elif len(self.log) > 1:
                self._write_result()
                self.log[_date] = 1
            else:
                self.log[_date] = 1

    def _write_result(self):
        # Открывать файл для записи каждой отдельной строки достаточно ресурсозатратно.
        #  Можно открыть файл для записи одн раз до начала цикла.
        # TODO данная функция вызывалась после чтения всего файла один раз, но до закрытия анализируемого файла
        #  сейчас переместил вызов и вызывается он после закрытия анализируемого файла
        with open(self.result_file, 'a', encoding='UTF8') as file:
            for item in self.log.items():
                file.write(f'{item[0]}] {item[1]}\n')
            self.log.clear()


new_log = LogParser(_log_file='events.txt', _group_type='m', _event='NOK')
new_log.run()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
new_log = LogParser(_log_file='events.txt', _group_type='h', _event='NOK')
new_log.run()
new_log = LogParser(_log_file='events.txt', _group_type='mm', _event='NOK')
new_log.run()
new_log = LogParser(_log_file='events.txt', _group_type='yy', _event='NOK')
new_log.run()
