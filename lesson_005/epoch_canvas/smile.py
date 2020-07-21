# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 900)


def smile(x, y, color):
    radius = 30
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
