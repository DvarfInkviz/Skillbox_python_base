# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 900)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

coordinates = []
for _ in range(N):
    coordinates.append([sd.random_number(200, 900), sd.random_number(800, 900), sd.random_number(10, 50)])

# TODO Часть 1!
while True:
    sd.clear_screen()
    for item in coordinates:
        point = sd.get_point(item[0], item[1])
        sd.snowflake(center=point, length=item[2])
        item[1] -= 10
        if item[1] < 50:
            break
        item[0] += 2
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# TODO часть 2!
# while True:
#     for item in coordinates:
#         sd.start_drawing()
#         point = sd.get_point(item[0], item[1])
#         sd.snowflake(center=point, length=item[2], color=sd.background_color)
#         item[1] -= 10
#         if item[1] < 5:
#             break
#         item[0] += 2
#         point = sd.get_point(item[0], item[1])
#         sd.snowflake(center=point, length=item[2])
#         sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# TODO часть 3! переменная i считает упавшие снежинки; досчитав до snow, программа дает возможность упасть
#  всем снежинкам на экране; одновременно падает N снежинок
# i = 0
# snow = 100
# while i < snow:
#     y = 0
#     while y < len(coordinates):
#         if len(coordinates) > 0:
#             item = coordinates[y]
#             # print(f'i= {i}, y= {y} из {len(coordinates)} - {item}')
#             sd.start_drawing()
#             point = sd.get_point(item[0], item[1])
#             sd.snowflake(center=point, length=item[2], color=sd.background_color)
#             item[1] -= sd.random_number(10, 20)
#             item[0] += sd.random_number(-3, 3)
#             point = sd.get_point(item[0], item[1])
#             sd.snowflake(center=point, length=item[2])
#             if item[1] < 10 + i:
#                 del coordinates[y]
#                 if y != 0:
#                     y -= 1
#                 if i < snow - 1:
#                     coordinates.append([sd.random_number(200, 900), sd.random_number(800, 900),
#                                         sd.random_number(10, 50)])
#                     i += 1
#                 continue
#             sd.finish_drawing()
#             y += 1
#     if len(coordinates) == 0:
#         i = snow
#         # print(f'i= {i}, y= {y} из {len(coordinates)} - {item}')
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
