# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1000)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(_point, _length=200, _angle=0):
    v1 = sd.get_vector(start_point=_point, angle=_angle, length=_length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=_angle + 120, length=_length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=_angle + 240, length=_length, width=3)
    v3.draw()


def square(_point, _length=200, _angle=0):
    v1 = sd.get_vector(start_point=_point, angle=_angle, length=_length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=_angle + 90, length=_length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=_angle + 180, length=_length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=_angle + 270, length=_length, width=3)
    v4.draw()


def pentagon(_point, _length=200, _angle=0):
    v1 = sd.get_vector(start_point=_point, angle=_angle, length=_length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=_angle + 72, length=_length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=_angle + 144, length=_length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=_angle + 216, length=_length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=_angle + 288, length=_length, width=3)
    v5.draw()


def hexagon(_point, _length=200, _angle=0):
    v1 = sd.get_vector(start_point=_point, angle=_angle, length=_length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=_angle + 60, length=_length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=_angle + 120, length=_length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=_angle + 180, length=_length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=_angle + 240, length=_length, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=_angle + 300, length=_length, width=3)
    v6.draw()


triangle(_point=sd.random_point(), _angle=23, _length=100)
square(_point=sd.random_point(), _angle=67, _length=100)
pentagon(_point=sd.random_point(), _angle=35, _length=100)
hexagon(_point=sd.random_point(), _angle=8, _length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)


#  вариант номер 2 с общей функцией
#  Второй вариант уменьшает дублирование кода недостаточно. Цикл нужно делать
#  в общей функции, т. е. то, что вы сделали в варианте 3.
def vector_draw(_point, _angle, _length, _width, _color=sd.COLOR_YELLOW):
    _vector = sd.get_vector(start_point=_point, angle=_angle, length=_length, width=_width)
    _vector.draw(color=_color)
    return _vector.end_point


def triangle_v2(_point, _length=200, _angle=0):
    _prv_point = _point
    for _i in range(3):
        if _i == 2:
            sd.line(start_point=_prv_point, end_point=_point, width=3, color=sd.random_color())
        else:
            _prv_point = vector_draw(_point=_prv_point, _length=_length, _angle=_angle + _i * 360 / 3, _width=3,
                                     _color=sd.random_color())


def square_v2(_point, _length=200, _angle=0):
    _prv_point = _point
    for _i in range(4):
        if _i == 3:
            sd.line(start_point=_prv_point, end_point=_point, width=3, color=sd.random_color())
        else:
            _prv_point = vector_draw(_point=_prv_point, _length=_length, _angle=_angle + _i * 360 / 4, _width=3,
                                     _color=sd.random_color())


def pentagon_v2(_point, _length=200, _angle=0):
    _prv_point = _point
    for _i in range(5):
        if _i == 4:
            sd.line(start_point=_prv_point, end_point=_point, width=3, color=sd.random_color())
        else:
            _prv_point = vector_draw(_point=_prv_point, _length=_length, _angle=_angle + _i * 360 / 5, _width=3,
                                     _color=sd.random_color())


def hexagon_v2(_point, _length=200, _angle=0):
    _prv_point = _point
    for _i in range(6):
        if _i == 5:
            sd.line(start_point=_prv_point, end_point=_point, width=3, color=sd.random_color())
        else:
            _prv_point = vector_draw(_point=_prv_point, _length=_length, _angle=_angle + _i * 360 / 6, _width=3,
                                     _color=sd.random_color())


triangle_v2(_point=sd.random_point(), _angle=23, _length=100)
square_v2(_point=sd.random_point(), _angle=67, _length=100)
pentagon_v2(_point=sd.random_point(), _angle=35, _length=100)
hexagon_v2(_point=sd.random_point(), _angle=8, _length=100)


# третий вариант с одной функцией, рисующей равносторонние n-угольники
def shape_draw(_point, _length=100, _angle=0, _n_corner=3, _color=sd.COLOR_YELLOW):
    prv_point = _point
    # TODO От проверки внутри цикла можно избавиться, если рисовать линию после цикла,
    #  уменьшив значение range на 1.
    for _i in range(_n_corner):
        if _i == _n_corner-1:
            sd.line(start_point=prv_point, end_point=_point, width=3, color=_color)
        else:
            vector = sd.get_vector(start_point=prv_point, angle=_angle + _i * 360 / _n_corner, length=_length, width=3)
            prv_point = vector.end_point
            vector.draw(color=_color)

# TODO Раз вы начали делать вторую часть, то добавьте отдельные функции
#  рисования фигур, в которых будет вызываться общая функция.


point = sd.get_point(900, 600)
for i in range(3, 15):
    shape_draw(_point=point, _length=200, _n_corner=i, _angle=(i-3)*15, _color=sd.random_color())
# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
