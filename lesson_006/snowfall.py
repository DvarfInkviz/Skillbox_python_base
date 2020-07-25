# -*- coding: utf-8 -*-

import simple_draw as sd

_coordinates = []
_over_screen = []


def add_snowflake(quantity):
    global _coordinates
    for _ in range(quantity):
        _coordinates.append([sd.random_number(0, sd.resolution[0]), sd.random_number(0, sd.resolution[1]),
                             sd.random_number(10, 50)])


def draw_snowflake(color):
    global _coordinates
    for item in _coordinates:
        point = sd.get_point(x=item[0], y=item[1])
        sd.snowflake(center=point, color=color, length=item[2])


def step_snowflake():
    global _coordinates
    for item in _coordinates:
        item[1] -= sd.random_number(10, 20)
        item[0] += sd.random_number(-5, 5)


def snowflake_over_screen():
    global _coordinates
    global _over_screen
    _over_screen.clear()
    for i, item in enumerate(_coordinates):
        if item[1] + item[2] < 0:
            _over_screen.append(i)
    _over_screen.reverse()


def del_snowflake(over_screen):
    global _coordinates
    for item in over_screen:
        del _coordinates[item]
