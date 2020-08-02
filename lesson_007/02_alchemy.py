# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы:
# Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Water, Air, Fire, Earth, Storm, Steam, Dirt, Lightning, Dust, Lava
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Human):
            return Corpse()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Human):
            return Farmer()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        return None


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        if isinstance(other, Human):
            return Sauna()
        else:
            return None


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        return None


class Lightning:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        return None


class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        return None


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        if isinstance(other, Human):
            return Corpse()
        else:
            return None


# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


class Human:
    def __str__(self):
        return 'Человек'

    def __add__(self, other):
        if isinstance(other, Lava) or isinstance(other, Fire):
            return Corpse()
        elif isinstance(other, Earth):
            return Farmer()
        elif isinstance(other, Steam):
            return Sauna()
        else:
            return None


class Corpse:
    def __str__(self):
        return 'Труп'

    def __add__(self, other):
        return None


class Farmer:
    def __str__(self):
        return 'Фермер'

    def __add__(self, other):
        return None


class Sauna:
    def __str__(self):
        return 'Сауна'

    def __add__(self, other):
        return None


print(Human(), '+', Steam(), '=', Human() + Steam())
print(Fire(), '+', Human(), '=', Fire() + Human())
print(Earth(), '+', Human(), '=', Earth() + Human())

# Зачёт!
