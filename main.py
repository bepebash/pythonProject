# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
#COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# TODO здесь ваш код
color = ()
print('Вы можете выбрать цвет рисуемых фигур.')
print('Если вы хотите красный цвет введите 1.')
print('Если вы хотите оранжевый цвет введите 2.')
print('Если вы хотите желтый цвет введите 3.')
print('Если вы хотите зеленый цвет введите 4.')
print('Если вы хотите голубой цвет введите 5.')
print('Если вы хотите синий цвет введите 6.')
print('Если вы хотите фиолетовый цвет введите 7.')
color_number = input('Введите здесть выбранный вами цвет')
if color_number == '1':
    color = sd.COLOR_RED
elif color_number == '2':
    color = sd.COLOR_ORANGE
elif color_number == '3':
    color = sd.COLOR_YELLOW
elif color_number == '4':
    color = sd.COLOR_GREEN
elif color_number == '5':
    color = sd.COLOR_CYAN
elif color_number == '6':
    color = sd.COLOR_BLUE
elif color_number == '7':
    color = sd.COLOR_PURPLE

print('Также вы можете выбрать фигуру для рисования (треугольник, квадрат, пятиугольник, шестиугольник')
figure = input ('Выберети желаемую фигуру')





def sixangle(point, angle, length, color):
    next_point = draw_side(start_point=point_six, angle = 0, length = 100, color = color)
    next_point = draw_side(start_point=next_point, angle =60, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =120, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =180, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =240, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =300, length =100, color = color)

def fiveangle(point, angle, length, color):
    next_point = draw_side(start_point=point_f, angle = 0, length = 100, color = color)
    next_point = draw_side(start_point=next_point, angle =72, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =144, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =216, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =288, length =100, color = color)

def triangle(point, angle, length, color):
    next_point = draw_side(start_point=point_t, angle = 0, length = 100, color = color)
    next_point = draw_side(start_point=next_point, angle =120, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =240, length =100, color = color)

def square(point, angle, length, color):
    next_point = draw_side(start_point=point_s, angle = 0, length = 100, color = color)
    next_point = draw_side(start_point=next_point, angle =90, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =180, length =100, color = color)
    next_point = draw_side(start_point=next_point, angle =270, length =100, color = color)

def draw_side(start_point, angle, length, color):
    v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
    v.draw(color = color)
    sd.circle(center_position=start_point,radius = 15)
    return v.end_point




if figure == 'треугольник':
    point_t = sd.get_point(100, 100)
    triangle(point_t,0,100, color)
elif figure == 'квадрат':
    point_s = sd.get_point(400, 100)
    square(point_s,0,100, color)
elif figure == 'пятиугольник':
    point_f = sd.get_point(100, 400)
    fiveangle(point_f,0,100, color)
elif figure == 'шестиугольник':
    point_six = sd.get_point(400,400)
    sixangle(point_six,0,100, color)
else:
    print('вы ввели несуществующую фигуру')



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
