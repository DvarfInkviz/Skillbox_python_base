# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 1000)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def shape_draw(_point, _length=100, _angle=0, _n_corner=3, _color=sd.COLOR_YELLOW):
    prv_point = _point
    for _i in range(_n_corner):
        if _i == _n_corner-1:
            sd.line(start_point=prv_point, end_point=_point, width=3, color=_color)
        else:
            vector = sd.get_vector(start_point=prv_point, angle=_angle + _i * 360 / _n_corner, length=_length, width=3)
            prv_point = vector.end_point
            vector.draw(color=_color)


colors = {
    1: sd.COLOR_RED,
    2: sd.COLOR_ORANGE,
    3: sd.COLOR_YELLOW,
    4: sd.COLOR_GREEN,
    5: sd.COLOR_CYAN,
    6: sd.COLOR_BLUE,
    7: sd.COLOR_PURPLE,
    8: sd.random_color(),
}

while True:
    user_input = input("Выберите цвет фигуры из следующего списка:\n1 : Красный\n2 : Оранжевый\n3 : Желтый\n4 : Зеленый"
                       "\n5 : Голубой\n6 : Синий\n7 : Фиолетовый\n8 : случайный \nВаш выбор >>")
    if user_input.isdigit():
        color = int(user_input)
        if 0 < color <= 8:
            print('Вы ввели', color)
            break
        else:
            print('Вы ввели некорректный номер цвета!')
    else:
        print('Вы ввели некорректный номер цвета!')

# Если использовать второй метод из первого задания, то вместо цикла будет вызвано 4 подряд функции построения фигур
for i in range(3, 7):
    point = sd.get_point(sd.random_number(100, 800), sd.random_number(100, 800))
    shape_draw(_point=point, _length=200, _n_corner=i, _angle=0, _color=colors[color])

sd.pause()
