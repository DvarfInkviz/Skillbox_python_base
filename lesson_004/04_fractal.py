# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 900)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(_point, _length, _angle=0):
    v1 = sd.get_vector(start_point=_point, angle=_angle + 30, length=_length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=_point, angle=_angle - 30, length=_length, width=3)
    v2.draw()


def draw_branches_recursion(start_point, _length, _angle=0):
    if _length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=_angle + 30, length=_length, width=3)
    v1.draw(color=sd.random_color())
    v2 = sd.get_vector(start_point=start_point, angle=_angle - 30, length=_length, width=3)
    v2.draw(color=sd.random_color())
    next_point = v1.end_point
    next_angle = _angle + 30
    next_length = _length * .75
    draw_branches_recursion(start_point=next_point, _angle=next_angle, _length=next_length)
    next_point = v2.end_point
    next_angle = _angle - 30
    next_length = _length * .75
    draw_branches_recursion(start_point=next_point, _angle=next_angle, _length=next_length)


# zero_point = sd.get_point(300, 0)
# root_point = sd.get_point(300, 30)
# sd.line(start_point=zero_point, end_point=root_point, width=3, color=(138, 102, 66))
# draw_branches_recursion(start_point=root_point, _angle=90, _length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


def draw_branches_recursion2(start_point, _length, _angle=0):
    if _length < 5:
        return
    if _length < 25:
        _color = (45, 114, 51)
        _width = 2
    else:
        _color = (138, 102, 66)
        _width = 4
    v1 = sd.get_vector(start_point=start_point, angle=_angle + 30, length=_length, width=_width)
    v1.draw(color=_color)
    v2 = sd.get_vector(start_point=start_point, angle=_angle - 30, length=_length, width=_width)
    v2.draw(color=_color)
    next_point = v1.end_point
    next_angle = _angle + sd.random_number(a=18, b=42)
    next_length = _length * sd.random_number(a=60, b=90) / 100
    draw_branches_recursion2(start_point=next_point, _angle=next_angle, _length=next_length)
    next_point = v2.end_point
    next_angle = _angle - sd.random_number(a=18, b=42)
    next_length = _length * sd.random_number(a=60, b=90) / 100
    draw_branches_recursion2(start_point=next_point, _angle=next_angle, _length=next_length)


zero_point = sd.get_point(600, 0)
root_point = sd.get_point(600, 70)
sd.line(start_point=zero_point, end_point=root_point, width=5, color=(138, 102, 66))
draw_branches_recursion2(start_point=root_point, _angle=90, _length=120)
sd.pause()
