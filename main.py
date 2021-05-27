# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
import random

sd.resolution = (800, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(coord_x, coord_y, color):
    point = sd.get_point(coord_x, coord_y)
    sd.circle(point, 50, color, 5)
    point_eye_left = sd.get_point(coord_x - 20, coord_y - 20)
    sd.circle(point_eye_left, 10)
    point_eye_right = sd.get_point(coord_x + 20, coord_y - 20)
    sd.circle(point_eye_right, 10)
    point_sm_st = sd.get_point(coord_x - 10, coord_y - 40)
    point_sm_en = sd.get_point(coord_x + 10, coord_y - 40)
    sd.line(point_sm_st, point_sm_en, color, 2)


for i in range(10):
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    smile(x, y, sd.random_color())

sd.pause()
