# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    no_cat_food = False
    no_food = False
    no_money = False
    total_food = 0
    total_cat_food = 0
    total_money = 0
    total_fur_coat = 0

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}, грязи {self.dirt}'


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = home
        self.dice = 0

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}, счастье {self.happiness}'

    def act(self):
        if (self.house.dirt > 90) and (self.__class__ != Child):
            self.happiness -= 10
        if self.fullness <= 0:
            # cprint(f'{self.name} умер от голода... R.I.P.', color='red')
            return
        if self.happiness < 10:
            # cprint(f'{self.name} умер от депрессии... R.I.P.', color='red')
            return
        self.dice = randint(1, 6)

    def eat(self):
        if self.house.food >= 10:
            if self.house.food >= 30:
                _b = 30
            else:
                _b = self.house.food
            _count = randint(a=10, b=_b)
            self.fullness += _count
            self.house.total_food += _count
            self.house.food -= _count
            # cprint(f'{self.name} поел (+{_count})', color='yellow')
        else:
            # cprint(f'{self.name}: нет еды! Жена должна сходить в магазин! (-10)', color='red')
            self.house.no_food = True
            self.fullness -= 10
            # if self.fullness <= 0:
            #     cprint(f'{self.name} умер от голода... R.I.P.', color='red')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10

    def pet_shop(self):
        if self.house.money >= 60:
            # cprint(f'{self.name} сходил в магазин за едой для кота', color='magenta')
            _count = randint(40, 60)
            self.house.money -= _count
            self.house.cat_food += _count
            self.house.no_cat_food = False
        else:
            # cprint(f'{self.name}: денег мало! Муж, иди работать! (-10)', color='red')
            self.house.no_money = True
        self.fullness -= 10


class Husband(Human):
    salary = 150

    def act(self):
        super().act()
        if (self.fullness > 0) and (self.happiness > 10):
            if self.house.no_money:
                self.work()
            elif self.fullness <= 20:
                self.eat()
            elif self.house.no_cat_food:
                self.pet_shop()
            elif self.happiness < 50:
                self.gaming()
            elif self.dice == 2:
                self.pet_the_cat()
            elif self.dice == 3:
                self.work()
            elif self.dice == 4:
                self.eat()
            else:
                self.gaming()

    def work(self):
        # cprint(f'{self.name} сходил на работу (-10, +150)', color='blue')
        self.house.money += self.salary
        self.house.total_money += self.salary
        self.fullness -= 10
        self.house.no_money = False

    def gaming(self):
        # cprint(f'{self.name} играл WoT целый день (-10, +20)', color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def act(self):
        super().act()
        if (self.fullness > 0) and (self.happiness > 10):
            if self.house.no_food:
                self.shopping()
            elif self.fullness <= 20:
                self.eat()
            elif self.house.no_cat_food:
                self.pet_shop()
            elif self.happiness < 70:
                self.buy_fur_coat()
            elif self.house.dirt > 90:
                self.clean_house()
            elif self.dice == 1:
                self.shopping()
            elif self.dice == 2:
                self.pet_the_cat()
            elif self.dice > 3:
                self.eat()
            self.house.dirt += 5

    def shopping(self):
        if self.house.money >= 50:
            if self.house.money > 80:
                _b = 80
            else:
                _b = self.house.money
            _count = randint(a=40, b=_b)
            self.house.money -= _count
            self.house.food += _count
            # cprint(f'{self.name} сходила в магазин за едой (-10, +{_count})', color='magenta')
            self.house.no_food = False
        else:
            # cprint(f'{self.name}: денег мало! Муж, иди работать! (-10)', color='red')
            self.house.no_money = True
        self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money >= 350:
            # cprint(f'{self.name} сходила в магазин за шубой (-10, + 60, -350)', color='magenta')
            self.house.money -= 350
            self.house.total_fur_coat += 1
            self.happiness += 60
        else:
            # cprint(f'{self.name}: мне грустно, хочу шубу, а денег мало! Муж, иди работать! (-10)', color='red')
            self.house.no_money = True
        self.fullness -= 10

    def clean_house(self):
        if self.house.dirt < 50:
            _a = 0
        else:
            _a = 50
        _b = self.house.dirt
        _count = randint(a=_a, b=_b)
        self.house.dirt -= _count
        self.fullness -= 10
        # cprint(f'{self.name} убиралась в доме (-10, -{_count})', color='magenta')


# Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = home

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def act(self):
        if self.fullness <= 0:
            # cprint('{} умер... R.I.P.'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 3:
            self.sleep()
        elif dice == 5:
            self.eat()
        else:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            _count = randint(a=1, b=10)
            self.fullness += _count * 2
            self.house.total_cat_food += _count
            self.house.cat_food -= _count
            # cprint(f'{self.name} поел', color='yellow')
        else:
            # cprint(f'{self.name}: нет еды в миске!', color='red')
            self.house.no_cat_food = True
            self.fullness -= 10
            # if self.fullness <= 0:
            #     cprint(f'{self.name} умер... R.I.P.', color='red')

    def sleep(self):
        # cprint(f'{self.name} спал целый день', color='green')
        self.fullness -= 10

    def soil(self):
        # cprint(f'{self.name} драл обои целый день', color='green')
        self.fullness -= 10
        self.house.dirt += 5


# Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


class Child(Human):

    def act(self):
        super().act()
        if self.fullness > 0:
            if self.fullness <= 20:
                self.eat()
            elif self.dice > 3:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        if self.house.food >= 5:
            _count = randint(a=5, b=10)
            self.fullness += _count
            self.house.total_food += _count
            self.house.food -= _count
            # cprint(f'{self.name} поел (+{_count})', color='yellow')
        else:
            # cprint(f'{self.name}: нет еды! Маме надо сходить в магазин! (-5)', color='red')
            self.house.no_food = True
            self.fullness -= 5
            # if self.fullness <= 0:
            #     cprint(f'{self.name} умер от голода... R.I.P.', color='red')

    def sleep(self):
        # cprint(f'{self.name} спал целый день (-10)', color='green')
        self.fullness -= 5


#  после реализации второй части - отдать на проверку учителем две ветки


# Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


class Simulation:

    def __init__(self, _money_incidents, _food_incidents):
        self.food_incidents = []
        self.money_incidents = []
        self.max_cats = 0
        for _ in range(_money_incidents):
            self.money_incidents.append(randint(1, 366))
        for _ in range(_food_incidents):
            self.food_incidents.append(randint(1, 366))

    def __str__(self):
        return f'food_incidents_days={self.food_incidents}, money_incidents_days={self.money_incidents}'

    def experiment(self, _salary):
        Husband.salary = _salary
        self.max_cats = len(cats)
        for _day in range(1, 366):
            if _day in self.food_incidents:
                House.total_food = 0
            if _day in self.money_incidents:
                House.total_money /= 2
            for _citizen in citizens:
                _citizen.act()
            for _cat in cats:
                _cat.act()
            for _citizen in citizens:
                if _citizen.fullness <= 0 and _citizen.name not in rips:
                    rips[_citizen.name] = _day
            for _cat in cats:
                if _cat.fullness <= 0 and _cat.name not in rips:
                    self.max_cats -= 1
                    rips[_cat.name] = _day
            if len(rips) == len(citizens) + len(cats):
                cprint(f'Все умерли на {_day} день. R.I.P.', color='red')
                return self.max_cats
        return self.max_cats


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов

for food_incidents in range(1, 6):
    for money_incidents in range(1, 6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            home = House()
            citizens = [
                Husband(name='Сережа'),
                Wife(name='Маша'),
                Child(name='Коля'),
            ]
            cats = [
                Cat(name='Мурзик'),
                Cat(name='Васька'),
                Cat(name='Шнурок'),
            ]
            rips = {}
            # print(life)
            max_cats = life.experiment(salary)
            if max_cats > 0:
                print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
