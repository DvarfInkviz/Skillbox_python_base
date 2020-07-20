# -*- coding: utf-8 -*-
import simple_draw as sd

from epoch_canvas.nature import sun


def go_sun(_delta):
    while True:
        sd.start_drawing()
        sun(_color=sd.background_color, _delta=_delta)
        _delta = sd.random_number(10, 45)
        sun(_delta=_delta)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
