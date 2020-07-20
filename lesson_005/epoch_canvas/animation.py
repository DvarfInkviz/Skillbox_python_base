# -*- coding: utf-8 -*-
import simple_draw as sd

from epoch_canvas.nature import draw_tree, sun

sd.resolution = (1200, 900)
sd.start_drawing()
draw_tree()
draw_tree(800, 100)
sun(_delta=12)
sd.finish_drawing()
delta = 12
while True:
    sd.start_drawing()
    sun(_color=sd.background_color, _delta=delta)
    delta = sd.random_number(10, 45)
    sun(_delta=delta)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
