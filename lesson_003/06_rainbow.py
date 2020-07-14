# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.
start_x = 50
start_y = 50
end_x = 350
end_y = 450
step = 5
width = 4
i = 0
for colors in rainbow_colors:
    start_point = sd.get_point(start_x + i * step, start_y)
    end_point = sd.get_point(end_x + i * step, end_y)
    sd.line(start_point=start_point, end_point=end_point, color=colors, width=width)
    i += 1

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
i = 0
for colors in rainbow_colors:
    point = sd.get_point(400, -100)
    radius = 600 - i * step
    sd.circle(center_position=point, radius=radius, width=width, color=colors)
    i += 1

sd.pause()
