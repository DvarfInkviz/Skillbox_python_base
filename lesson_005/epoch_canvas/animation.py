# -*- coding: utf-8 -*-
import simple_draw as sd

from epoch_canvas.nature import sun, cloud, rainbow
from epoch_canvas.smile import smile, sad_smile

N = 10
rainbow_colors = [
    (sd.COLOR_DARK_RED, sd.COLOR_DARK_ORANGE, sd.COLOR_DARK_YELLOW, sd.COLOR_DARK_GREEN, sd.COLOR_DARK_CYAN,
     sd.COLOR_DARK_BLUE, sd.COLOR_DARK_PURPLE),
    (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE),
]


def go_go(_sleep):
    sd.take_background()
    cloud_length = 160
    while True:
        x = -500
        coordinates = []
        for _ in range(N):
            coordinates.append([sd.random_number(x-50, x+cloud_length), sd.random_number(660, 670),
                                sd.random_number(10, 50)])
        while x < sd.resolution[0]+cloud_length*3:
            if x == -152:
                sd.draw_background()
                sad_smile(x=480, y=125, color=sd.COLOR_DARK_ORANGE)
                sd.take_background()
            if x == sd.resolution[0] + cloud_length*1.5:
                sd.draw_background()
                smile(x=480, y=125, color=sd.COLOR_YELLOW)
                sd.take_background()
            coordinates.append([sd.random_number(x-50, x+cloud_length), sd.random_number(660, 670),
                                sd.random_number(10, 30)])
            sd.start_drawing()
            sd.draw_background()
            _delta = sd.random_number(10, 45)
            x += 4
            sun(_delta=_delta)
            if x % 10 == 0:
                rainbow(rainbow_colors[0])
            else:
                rainbow(rainbow_colors[1])
            cloud(_x=x)
            for i, item in enumerate(coordinates):
                point = sd.get_point(item[0], item[1])
                sd.snowflake(center=point, length=item[2])
                if item[1] < 10:
                    del coordinates[i]
                    if i != 0:
                        i -= 1
                    coordinates.append([sd.random_number(x-50, x + cloud_length), sd.random_number(660, 670),
                                        sd.random_number(10, 30)])
                item[1] -= sd.random_number(10, 20)
                item[0] += sd.random_number(-5, 5)
            sd.finish_drawing()
            sd.sleep(_sleep)
        if sd.user_want_exit():
            break
