# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO Ключевой элемент этого задания заключается в использовании нескольких функций
#  и выбора одной их них для рисования фигур.
#  Будет удобно создать словарь в значениях которого будут храниться
#  названием фигур и ссылками на функции, а ключами словаря будут цифры,
#  вводимые пользователем.
#  Ссылки на функции, проще говоря их названия, можно поместить в структуру данных:
#  список, кортеж, словарь, ... На примере списков это работает так:
#  functs = [pentagon, hexagon, triangle]
#  draw_function = functs[0]
#  draw_function(start_point, start_angle, length



def shape_draw(_point, _length=100, _angle=0, _n_corner=3, _color=sd.COLOR_YELLOW):
    prv_point = _point
    for _i in range(_n_corner):
        if _i == _n_corner-1:
            sd.line(start_point=prv_point, end_point=_point, width=3, color=_color)
        else:
            vector = sd.get_vector(start_point=prv_point, angle=_angle + _i * 360 / _n_corner, length=_length, width=3)
            prv_point = vector.end_point
            vector.draw(color=_color)


while True:
    user_input = input("Выберите фигуру из следующего списка:\n1 : Треугольник\n2 : Квадрат\n3 : Пятиугольник"
                       "\n4 : Шестиугольник\n5 : Произвольный n-угольник\nВаш выбор >>")
    if user_input.isdigit():
        corners = int(user_input)
        if 0 < corners <= 5:
            print('Вы ввели', corners)
            if corners == 5:
                corners = sd.random_number(3, 15)
                print(f'Будет построен правильный {corners}-угольник')
            else:
                corners += 2
            break
        else:
            print('Вы ввели некорректный номер фигуры!')
    else:
        print('Вы ввели некорректный номер фигуры!')

point = sd.get_point(300, 300)
shape_draw(_point=point, _length=50, _n_corner=corners, _angle=sd.random_number(10, 50), _color=sd.COLOR_YELLOW)
# при использовании второго метода из первого задания пришлось бы писать условия if/elif/else для выбора нужной функции
sd.pause()
