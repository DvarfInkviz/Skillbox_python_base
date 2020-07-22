# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as residents_room_1
from room_2 import folks as residents_room_2

separator = ', '
print(f'В комнате room_1 живут: {separator.join(residents_room_1)}')
print(f'В комнате room_2 живут: {separator.join(residents_room_2)}')

# Зачёт!
