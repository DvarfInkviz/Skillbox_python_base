# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as room1
from district.central_street.house1 import room2 as room2
from district.central_street.house2 import room1 as room3
from district.central_street.house2 import room2 as room4
from district.soviet_street.house1 import room1 as room5
from district.soviet_street.house1 import room2 as room6
from district.soviet_street.house2 import room1 as room7
from district.soviet_street.house2 import room2 as room8

separator = ', '
residents = room1.folks + room2.folks + room3.folks + room4.folks + room5.folks + room6.folks + room7.folks + \
            room8.folks
print(f'На районе живут {separator.join(residents)}')
