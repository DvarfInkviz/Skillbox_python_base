# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def shape_draw(_point, _length=100, _angle=0, _n_corner=3, _color=sd.COLOR_YELLOW):
    prv_point = _point
    for _i in range(_n_corner-1):
        vector = sd.get_vector(start_point=prv_point, angle=_angle + _i * 360 / _n_corner, length=_length, width=3)
        prv_point = vector.end_point
        vector.draw(color=_color)
    sd.line(start_point=prv_point, end_point=_point, width=3, color=_color)


def triangle(_point, _length=200, _angle=0):
    shape_draw(_point=_point, _length=_length, _angle=_angle, _n_corner=3, _color=sd.random_color())


def square(_point, _length=200, _angle=0):
    shape_draw(_point=_point, _length=_length, _angle=_angle, _n_corner=4, _color=sd.random_color())


def pentagon(_point, _length=200, _angle=0):
    shape_draw(_point=_point, _length=_length, _angle=_angle, _n_corner=5, _color=sd.random_color())


def hexagon(_point, _length=200, _angle=0):
    shape_draw(_point=_point, _length=_length, _angle=_angle, _n_corner=6, _color=sd.random_color())


shapes = {
    '1': ['Треугольник', triangle],
    '2': ['Квадрат', square],
    '3': ['Пятиугольник', pentagon],
    '4': ['Шестиугольник', hexagon],
}
while True:
    user_input = input("Выберите фигуру из следующего списка:\n1 : Треугольник\n2 : Квадрат\n3 : Пятиугольник"
                       "\n4 : Шестиугольник\n5 : Произвольный n-угольник\nВаш выбор >>")
    if user_input in shapes:
        shape = shapes[user_input]
        print('Вы выбрали ', shape[0])
        break
    else:
        print('Вы ввели некорректный номер фигуры!')

point = sd.get_point(300, 300)
draw_function = shape[1]
draw_function(_point=point, _length=50, _angle=sd.random_number(10, 50))

sd.pause()
