# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 900)


def shape_draw(_point, _length=100, _angle=0, _n_corner=3, _color=sd.COLOR_YELLOW):
    prv_point = _point
    for _i in range(_n_corner-1):
        vector = sd.get_vector(start_point=prv_point, angle=_angle + _i * 360 / _n_corner, length=_length, width=3)
        prv_point = vector.end_point
        vector.draw(color=_color)
    sd.line(start_point=prv_point, end_point=_point, width=3, color=_color)


def smile(x, y, color):
    radius = 50
    _point = sd.get_point(x=x, y=y)
    sd.circle(center_position=_point, radius=radius, width=3, color=sd.COLOR_BLACK)
    sd.circle(center_position=_point, radius=radius-2, width=0, color=color)
    left_point = sd.get_point(x=x - radius // 3, y=y + radius // 3)
    right_point = sd.get_point(x=x - radius // 5, y=y + 2 * radius // 3)
    sd.ellipse(left_bottom=left_point, right_top=right_point, color=sd.COLOR_BLACK)
    left_point = sd.get_point(x=x + radius // 5, y=y + radius // 3)
    right_point = sd.get_point(x=x + radius // 3, y=y + 2 * radius // 3)
    sd.ellipse(left_bottom=left_point, right_top=right_point, color=sd.COLOR_BLACK)
    left_point = sd.get_point(x=x - radius // 2, y=y - radius // 3)
    right_point = sd.get_point(x=x + radius // 2, y=y - radius // 3)
    sd.line(start_point=left_point, end_point=right_point, width=3, color=sd.COLOR_BLACK)


point = sd.get_point(500, 200)
shape_draw(_point=point, _length=5, _n_corner=40)
sd.pause()
