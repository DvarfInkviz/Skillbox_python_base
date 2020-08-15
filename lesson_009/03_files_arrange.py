# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class FileSorter:

    def __init__(self, _scan_dir):
        self.scan_dir = os.path.normpath(_scan_dir)
        self.result_dir = 'icons_by_year'

    def run(self):
        if self.scan_dir.endswith('.zip'):
            self.unzip()
        else:
            self.scan()
        print('All Done!')

    def unzip(self):
        with zipfile.ZipFile(self.scan_dir, 'r') as _zip_file:
            for _file in _zip_file.infolist():
                if _file.filename[-1] != '/':
                    _file.filename = os.path.basename(_file.filename)
                    _dst = os.path.join(self.result_dir, str(_file.date_time[0]), str(_file.date_time[1]))
                    os.makedirs(name=_dst, exist_ok=True)
                    _zip_file.extract(member=_file, path=_dst)

    def scan(self):
        for _dirpath, _dirnames, _filenames in os.walk(self.scan_dir):
            for _file in _filenames:
                _full_file_path = os.path.join(_dirpath, _file)
                _secs = os.path.getmtime(_full_file_path)
                _file_time = time.gmtime(_secs)
                _dst = os.path.join(self.result_dir, str(_file_time[0]), str(_file_time[1]))
                os.makedirs(name=_dst, exist_ok=True)
                shutil.copy2(src=_full_file_path, dst=_dst)


new_sort = FileSorter(_scan_dir='icons')
new_sort.run()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
#
new_sort = FileSorter(_scan_dir='icons.zip')
new_sort.run()

# Зачёт!
