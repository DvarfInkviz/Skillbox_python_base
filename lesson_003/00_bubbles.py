# -*- coding: utf-8 -*-

import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)
radius = 100
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(_point, _step, _width, _color):
    _radius = 50
    for _ in range(3):
        _radius += step
        sd.circle(center_position=_point, radius=_radius, width=_width, color=_color)


point = sd.get_point(100, 100)
bubble(_point=point, _step=7, _width=1, _color=(255, 0, 45))

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1100, 100):
    point = sd.get_point(x, 200)
    bubble(_point=point, _step=7, _width=2, _color=(205, 0, 145))

# Нарисовать три ряда по 10 пузырьков
for y in range(300, 600, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(_point=point, _step=7, _width=2, _color=sd.random_color())

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 15)
    bubble(_point=point, _step=step, _width=2, _color=sd.random_color())

sd.pause()


