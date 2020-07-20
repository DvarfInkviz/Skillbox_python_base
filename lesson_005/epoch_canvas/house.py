# -*- coding: utf-8 -*-
import simple_draw as sd


def draw_house(_x=300, _y=10):
    brick_height = 50
    brick_length = 100
    brick_seam = 6
    brick_color = (136, 69, 53)
    seam_color = (104, 108, 94)
    bottom_point = sd.get_point(_x, _y)
    top_point = sd.get_point(x=_x + 300, y=_y + 200)
    sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=brick_color)
    triangle = [
        sd.Point(_x - 50, _y + 200),
        sd.Point(_x + 350, _y + 200),
        sd.Point(_x + 150, _y + 300),
    ]
    sd.polygon(point_list=triangle, width=0, color=seam_color)

    # for x in range(5, 1200, brick_seam + brick_length):
    #     for y in range(5, 600, brick_seam + brick_height):
    #         bottom_point = sd.get_point(x=x, y=y)
    #         line_point1 = sd.get_point(x=0, y=y-2)
    #         line_point2 = sd.get_point(x=1200, y=y-2)
    #         top_point = sd.get_point(x=x+brick_length, y=y+brick_height)
    #         sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=brick_color)
    #         sd.line(start_point=line_point1, end_point=line_point2, color=seam_color, width=brick_seam)
    #     line_point1 = sd.get_point(x=x-4, y=0)
    #     line_point2 = sd.get_point(x=x-4, y=600)
    #     sd.line(start_point=line_point1, end_point=line_point2, color=seam_color, width=brick_seam)
