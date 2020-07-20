# -*- coding: utf-8 -*-
import simple_draw as sd


def sun(_x=200, _y=700):
    point = sd.get_point(x=_x, y=_y)
    sd.start_drawing()
    sd.circle(center_position=point, width=0)
    for i in range(8):
        vector = sd.get_vector(start_point=point, angle=0+i*45, length=100, width=4)
        vector.draw()
    sd.finish_drawing()
    delta = 0
    while True:
        sd.start_drawing()
        for i in range(8):
            vector = sd.get_vector(start_point=point, angle=0 + i * 45 + delta, length=100, width=4)
            vector.draw(color=sd.background_color)
        delta = sd.random_number(10, 45)
        sd.circle(center_position=point, width=0)
        for i in range(8):
            vector = sd.get_vector(start_point=point, angle=0 + i * 45 + delta, length=100, width=4)
            vector.draw()
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


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
    next_length = _length * sd.random_number(a=60, b=90) / 100
    draw_branches(start_point=next_point, _angle=next_angle, _length=next_length)
    next_point = v2.end_point
    next_angle = _angle - sd.random_number(a=18, b=42)
    next_length = _length * sd.random_number(a=60, b=90) / 100
    draw_branches(start_point=next_point, _angle=next_angle, _length=next_length)


sd.resolution = (1200, 900)
sd.start_drawing()
zero_point = sd.get_point(600, 0)
root_point = sd.get_point(600, 70)
sd.line(start_point=zero_point, end_point=root_point, width=5, color=(138, 102, 66))
draw_branches(start_point=root_point, _angle=90, _length=50)
sd.finish_drawing()
sun()
sd.pause()
