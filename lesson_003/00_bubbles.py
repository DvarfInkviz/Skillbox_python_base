# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)
radius = 100
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, width, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=width, color=color)


point = sd.get_point(100, 100)
bubble(point=point, step=7, width=1, color=(255, 0, 45))

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1100, 100):
    point = sd.get_point(x, 200)
    bubble(point=point, step=7, width=2, color=(205, 0, 145))

# Нарисовать три ряда по 10 пузырьков
for y in range(300, 600, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=7, width=2, color=(106, 50, 145))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 15)
    bubble(point=point, step=step, width=2, color=sd.random_color())

sd.pause()


