#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Alexander', 'Natalia', 'Kristina', 'Mark', 'Mar\'ya', 'Marpha']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Alexander', 182],
    ['Natalia', 168],
    ['Kristina', 140],
    ['Mark', 110],
    ['Mar\'ya', 86],
    ['Marpha', 86],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост отца - {my_family_height[0][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

all_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + \
             my_family_height[4][1] + my_family_height[5][1]

print(f'Общий рост моей семьи - {all_height} см')

# Зачёт!
