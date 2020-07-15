# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    radius = 50
    point = sd.get_point(x=x, y=y)
    sd.circle(center_position=point, radius=radius, width=3, color=sd.COLOR_BLACK)
    sd.circle(center_position=point, radius=radius-2, width=0, color=color)
    left_point = sd.get_point(x=x - radius // 3, y=y + radius // 3)
    right_point = sd.get_point(x=x - radius // 5, y=y + 2 * radius // 3)
    sd.ellipse(left_bottom=left_point, right_top=right_point, color=sd.COLOR_BLACK)
    left_point = sd.get_point(x=x + radius // 5, y=y + radius // 3)
    right_point = sd.get_point(x=x + radius // 3, y=y + 2 * radius // 3)
    sd.ellipse(left_bottom=left_point, right_top=right_point, color=sd.COLOR_BLACK)
    left_point = sd.get_point(x=x - radius // 2, y=y - radius // 3)
    right_point = sd.get_point(x=x + radius // 2, y=y - radius // 3)
    sd.line(start_point=left_point, end_point=right_point, width=3, color=sd.COLOR_BLACK)


for _ in range(10):
    smile(sd.random_number(50, 500), sd.random_number(50, 500), sd.random_color())
sd.pause()

# Зачёт!
