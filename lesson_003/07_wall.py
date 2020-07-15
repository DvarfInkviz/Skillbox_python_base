# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич
sd.resolution = (1200, 600)
brick_height = 50
brick_length = 100
brick_seam = 6
brick_color = (136, 69, 53)
seam_color = (104, 108, 94)
for x in range(5, 1200, brick_seam + brick_length):
    for y in range(5, 600, brick_seam + brick_height):
        bottom_point = sd.get_point(x=x, y=y)
        line_point1 = sd.get_point(x=0, y=y-2)
        line_point2 = sd.get_point(x=1200, y=y-2)
        top_point = sd.get_point(x=x+brick_length, y=y+brick_height)
        sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=brick_color)
        sd.line(start_point=line_point1, end_point=line_point2, color=seam_color, width=brick_seam)
    line_point1 = sd.get_point(x=x-4, y=0)
    line_point2 = sd.get_point(x=x-4, y=600)
    sd.line(start_point=line_point1, end_point=line_point2, color=seam_color, width=brick_seam)
sd.pause()

# Зачёт!
