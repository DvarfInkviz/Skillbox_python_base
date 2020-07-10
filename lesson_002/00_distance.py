#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']
msk_lnd = ((moscow[0]-london[0]) ** 2 + (moscow[1]-london[1]) ** 2) ** 0.5
msk_prs = ((moscow[0]-paris[0]) ** 2 + (moscow[1]-paris[1]) ** 2) ** 0.5
prs_lnd = ((paris[0]-london[0]) ** 2 + (paris[1]-london[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = msk_lnd
distances['Moscow']['Paris'] = msk_prs
distances['London'] = {}
distances['London']['Moscow'] = msk_lnd
distances['London']['Paris'] = prs_lnd
distances['Paris'] = {}
distances['Paris']['Moscow'] = msk_prs
distances['Paris']['London'] = prs_lnd

print(distances)




