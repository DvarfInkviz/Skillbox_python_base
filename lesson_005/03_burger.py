# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
from random import randint

import my_burger

print('Начнем собирать двойной чизбургер по рецепту McDonald\'s Corporation...')
my_burger.add_bun()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_pickle()
my_burger.add_ketchup()
my_burger.add_onion()
my_burger.add_mustard()
my_burger.add_bun()
print('...и закончили. Пора есть!\n')

ingredients = {
    0: my_burger.add_bun,
    1: my_burger.add_patty,
    2: my_burger.add_ketchup,
    3: my_burger.add_cheese,
    4: my_burger.add_onion,
    5: my_burger.add_mustard,
    6: my_burger.add_pickle,
    7: my_burger.add_grill,
    8: my_burger.add_souce,
    9: my_burger.add_tomato,
}

print('Создаем мега фкусный бургер по секретному рецепту шеф-повара:')
item = ingredients[0]
item()
for i in range(10):
    item = ingredients[randint(1, 9)]
    item()
item = ingredients[0]
item()

# Зачёт!
