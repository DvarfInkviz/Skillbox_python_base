# -*- coding: utf-8 -*-
import simple_draw as sd


def draw_house(_x=300, _y=10):
    house_length = 300
    house_height = 200
    brick_height = 10
    brick_length = 30
    brick_seam = 3
    brick_color = (136, 69, 53)
    seam_color = (104, 108, 94)
    bottom_point = sd.get_point(_x, _y)
    top_point = sd.get_point(x=_x + house_length, y=_y + house_height)
    sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=brick_color)
    triangle = [
        sd.Point(_x - 50, _y + house_height),
        sd.Point(_x + house_length + 50, _y + house_height),
        sd.Point(_x + house_length // 2, _y + house_length),
    ]
    sd.polygon(point_list=triangle, width=0, color=seam_color)
    for y in range(house_height // brick_height):
        if y % 2 == 0:
            start_x = _x + brick_length
        else:
            start_x = _x + brick_length // 2
        if 0 < y < house_height // brick_height:
            line_point1 = sd.get_point(x=_x, y=_y+y*brick_height)
            line_point2 = sd.get_point(x=_x+house_length-1, y=_y+y*brick_height)
            sd.line(start_point=line_point1, end_point=line_point2, color=seam_color, width=brick_seam)
        for x in range(start_x, _x + house_length, brick_length + brick_seam):
            line_point1 = sd.get_point(x=x, y=_y+y*brick_height)
            line_point2 = sd.get_point(x=x, y=_y+(y+1)*brick_height)
            sd.line(start_point=line_point1, end_point=line_point2, color=seam_color, width=brick_seam)
    bottom_point = sd.get_point(x=_x+(brick_length+brick_seam)*3, y=_y+(brick_height+brick_seam)*6)
    top_point = sd.get_point(x=_x+(brick_length+brick_seam)*6, y=_y+(brick_height+brick_seam)*12)
    sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=(157, 161, 170))
    sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=(138, 102, 66), width=4)
