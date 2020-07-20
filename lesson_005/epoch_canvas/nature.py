# -*- coding: utf-8 -*-
import simple_draw as sd


def sun(_x=200, _y=700, _color=sd.COLOR_YELLOW, _delta=0):
    point = sd.get_point(x=_x, y=_y)
    sd.circle(center_position=point, width=0)
    for i in range(8):
        _vector = sd.get_vector(start_point=point, angle=0+i*45+_delta, length=100, width=4)
        _vector.draw(color=_color)


def draw_branches(start_point, _length, _angle=0):
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
    next_length = _length * sd.random_number(a=65, b=85) / 100
    draw_branches(start_point=next_point, _angle=next_angle, _length=next_length)
    next_point = v2.end_point
    next_angle = _angle - sd.random_number(a=18, b=42)
    next_length = _length * sd.random_number(a=65, b=85) / 100
    draw_branches(start_point=next_point, _angle=next_angle, _length=next_length)


def draw_tree(_x=600, _y=0):
    zero_point = sd.get_point(_x, _y)
    root_point = sd.get_point(_x, _y+70)
    sd.line(start_point=zero_point, end_point=root_point, width=5, color=(138, 102, 66))
    draw_branches(start_point=root_point, _angle=90, _length=50)
