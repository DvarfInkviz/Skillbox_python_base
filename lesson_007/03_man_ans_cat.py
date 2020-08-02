# -*- coding: utf-8 -*-

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint


class Cat:
    def __init__(self):
        self.name = None
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - кот {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{}: нет еды в миске!'.format(self.name), color='red')
            self.fullness -= 10
            if self.fullness <= 0:
                cprint('{} умер... R.I.P.'.format(self.name), color='red')

    def cat_sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def tears_wallpaper(self):
        cprint('{} драл обои целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер... R.I.P.'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 3:
            self.cat_sleep()
        elif dice == 5:
            self.eat()
        else:
            self.tears_wallpaper()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{}: нет еды!'.format(self.name), color='red')
            self.fullness -= 10
            if self.fullness <= 0:
                cprint('{} умер... R.I.P.'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{}: деньги кончились!'.format(self.name), color='red')
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='cyan')

    def take_cat(self, _cat, house, nickname):
        self.cat = _cat
        self.cat.house = house
        self.cat.name = nickname
        cprint('{} подобрал кота "{}"'.format(self.name, self.cat.name), color='cyan')

    def cleaning(self):
        self.house.dirt -= 100
        self.fullness -= 20

    def pet_shop(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{}: деньги кончились!'.format(self.name), color='red')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер... R.I.P.'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.pet_shop()
        elif self.house.dirt > 100:
            self.cleaning()
        elif dice == 2:
            self.work()
        elif dice == 4:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}\nЕды для кота {}, грязи {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]
cats = [
    Cat(),
    Cat(),
]
rips = {}

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

day_x = randint(1, 50)
my_cat = Cat()

for day in range(1, 732):
    if day == day_x:
        for i, cat in enumerate(cats):
            citizens[i].take_cat(_cat=cat, house=my_sweet_home, nickname='Васька_'+str(i))
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        if citizen.fullness > 0:
            citizen.act()
    if day >= day_x:
        for cat in cats:
            if cat.fullness > 0:
                cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        if citizen.fullness > 0:
            print(citizen)
        elif citizen.name not in rips:
            rips[citizen.name] = day
    if day >= day_x:
        for cat in cats:
            if cat.fullness > 0:
                print(cat)
            elif cat.name not in rips:
                rips[cat.name] = day
    print(my_sweet_home)
    if len(rips) == len(citizens)+len(cats):
        cprint('Все умерли на {} день. R.I.P.'.format(day), color='red')
        for item in rips.items():
            cprint('{} прожил {} дней'.format(item[0], item[1]), color='red')
        break
if len(rips) < len(citizens)+len(cats):
    for item in rips.items():
        cprint('{} прожил {} дней'.format(item[0], item[1]), color='red')

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
# TODO добавил реалистичности: когда люди ходят в магазин, у них уменьшается сытость. Если кто-то хотел поесть,
#  а еды нет, то у него тоже сытость уменьшается, так как он прожил день.
#  Чаще они могут прожить 365 дней, но кто-то обязательно умрет. Бывает, что никто не выживает за год
