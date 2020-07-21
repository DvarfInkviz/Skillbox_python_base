# -*- coding: utf-8 -*-
import simple_draw as sd

from epoch_canvas.nature import sun, cloud


def go_go(_delta):
    while True:
        x = -100
        while x < sd.resolution[0]+60:
            sd.start_drawing()
            sun(_color=sd.background_color, _delta=_delta)
            cloud(_x=x, _color=sd.background_color)
            _delta = sd.random_number(10, 45)
            x += 5
            sun(_delta=_delta)
            cloud(_x=x)
            sd.finish_drawing()
            sd.sleep(0.01)
        if sd.user_want_exit():
            break
