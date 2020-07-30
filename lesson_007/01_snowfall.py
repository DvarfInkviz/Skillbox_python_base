# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.resolution[0] // 2
        self.y = sd.resolution[1] - 10
        self.length = 20
        self.color = sd.COLOR_WHITE
        self.factor_a = 0.6
        self.factor_b = 0.35
        self.factor_c = 60

    def move(self):
        self.x += sd.random_number(a=-10, b=+10)
        self.y -= sd.random_number(a=10, b=30)
        self.color = sd.COLOR_RED

    def draw(self):
        point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=point, color=self.color, length=self.length, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    def clear_previous_picture(self):
        self.color = sd.background_color
        Snowflake.draw(self)

    def can_fall(self):
        return False if (self.y + self.length) < 0 else True


# flake = Snowflake()
# flake.x = 300
# flake.y = 600

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count):
    res = []
    for _ in range(count):
        _flake = Snowflake()
        _flake.x = sd.random_number(a=0, b=sd.resolution[0])
        _flake.y = sd.random_number(a=sd.resolution[1]-30, b=sd.resolution[1])
        res.append(_flake)
    return res


def get_fallen_flakes():
    res = 0
    for i, _flake in enumerate(flakes):
        if not _flake.can_fall():
            del flakes[i]
            res += 1
    return res


def append_flakes(count):
    for _ in range(count):
        _flake = Snowflake()
        _flake.x = sd.random_number(a=0, b=sd.resolution[0])
        _flake.y = sd.random_number(a=sd.resolution[1]-30, b=sd.resolution[1])
        flakes.append(_flake)


N = 50
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
