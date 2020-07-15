# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)
# TODO Условия нужно упростить. Некоторые условия записана по два раза.
#  Здесь достаточно сделать две проверки. В первой проверить что две стороны
#  листа меньше или равны размеру конверта, и если проверка не прошла
#  повернуть лист на 90 градусов и проверить ещё раз.
#  Сформулируйте условия также как во второй части этого задания.
if paper_x <= envelop_x:
    if paper_y <= envelop_y:
        print('ДА')
    elif paper_y <= envelop_x:
        if paper_x <= envelop_y:
            print('ДА')
        else:
            print('НЕТ')
elif paper_x <= envelop_y:
    if paper_y <= envelop_x:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

#  попытка написать решение с применением одного условия в if
#  получается очень громоздким
#  Да, так проверки лучше не делать.
# if brick_x <= hole_x:  # x-y
#     if brick_y <= hole_y:  # x-y
#         print('ДА')
#     elif brick_y <= hole_x:  # y-x
#         if brick_x <= hole_y:  # y-x
#             print('ДА')
#         elif brick_z <= hole_y:  # y-z
#             print('ДА')
#         else:
#             print('НЕТ')
#     elif brick_z <= hole_y:  # x-z
#         print('ДА')
#     elif brick_z <= hole_x:  # z-x
#         if brick_x <= hole_y:  # z-x
#             print('ДА')
#         else:
#             print('НЕТ')
#     else:
#         print('НЕТ')
# elif brick_x <= hole_y:  # y-x
#     if brick_y <= hole_x:  # y-x
#         print('ДА')
#     elif brick_z <= hole_x:  # z-x
#         print('ДА')
#     else:
#         pass
# elif brick_z <= hole_x:  #
#     pass
# elif brick_z <= hole_y:
#     pass
# else:
#     print('НЕТ')

#  решение с несколькими условиями в if
#  условий много, но если разложить нашу задачу на возможные варианты ее решения,
#  то они оказываются легки для понимания
#     ____
#    |    | hole_y
#    |____|
#     hole_x
#  возможные варианты расположения кирпича (x = brick_x, y = brick_y, z = brick_z)
#     ____         ____
#    |___| y  or  |___| x
#      x            y
#     ____         ____
#    |___| x  or  |___| z
#      z            x
#     ____         ____
#    |___| y  or  |___| z
#      z            y
#  всего 6 вариантов! которые легко описать в условиях

if ((brick_x <= hole_x) and (brick_y <= hole_y)) or ((brick_x <= hole_y) and (brick_y <= hole_x)):
    print('ДА')
elif ((brick_z <= hole_x) and (brick_x <= hole_y)) or ((brick_z <= hole_y) and (brick_x <= hole_x)):
    print('ДА')
elif ((brick_z <= hole_x) and (brick_y <= hole_y)) or ((brick_z <= hole_y) and (brick_y <= hole_x)):
    print('ДА')
else:
    print('НЕТ')
