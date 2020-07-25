# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

from snowfall import add_snowflake, draw_snowflake, step_snowflake, _over_screen, del_snowflake, \
    snowflake_over_screen

add_snowflake(50)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflake(color=sd.background_color)
    #  сдвинуть_снежинки()
    step_snowflake()
    #  нарисовать_снежинки_цветом(color)
    draw_snowflake(color=None)
    snowflake_over_screen()
    if len(_over_screen) > 0:
        del_snowflake(_over_screen)
        # TODO Нужно удалять столько снежинок, сколько было удалено перед этим.
        add_snowflake(10)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# TODO Исправьте замечания в модуле snowfall.
