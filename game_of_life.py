# Импорты
import time

import pygame as p
import random
from pygame.locals import *
import numpy as np

# Константы цветов RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Создаем окно
root = p.display.set_mode((1000, 500))


# 2х мерный список с помощью генераторных выражений
# cells = [[random.choice([0 , 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]

def choice(n):
    if n == 1:
        cells = np.zeros((25, 50))
        cells[10, 10:12] = 1
        cells[11, 10:12] = 1

    elif n == 2:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 10:12] = 1
        cells[12, 9:11] = 1

    elif n == 3:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 9] = 1
        cells[12, 9] = 1
        cells[13, 9] = 1
        cells[14, 9] = 1
        cells[15, 10] = 1
        cells[16, 10] = 1
        cells[17, 9] = 1
        cells[18, 9] = 1
        cells[19, 9] = 1
        cells[20, 9] = 1
        cells[21, 10] = 1

    elif n == 4:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 10] = 1
        cells[12, 10] = 1

    elif n == 5:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 11] = 1
        cells[12, 9:12] = 1

    else:
        cells = [[random.choice([0, 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]
    return cells


cells = choice(5)



# Функция определения кол-ва соседей
def near(pos: list, system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count


# Основной цикл
while 1:
    # Заполняем экран белым цветом
    root.fill(WHITE)

    # Рисуем сетку
    for i in range(0, root.get_height() // 20):
        p.draw.line(root, BLACK, (0, i * 20), (root.get_width(), i * 20))
    for j in range(0, root.get_width() // 20):
        p.draw.line(root, BLACK, (j * 20, 0), (j * 20, root.get_height()))
    # Нужно чтобы виндовс не думал что программа "не отвечает"
    for i in p.event.get():
        if i.type == QUIT:
            quit()
    # Проходимся по всем клеткам

    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            print(cells[i][j], i, j)
            p.draw.rect(root, (255 * cells[i][j] % 256, 0, 0), [i * 20, j * 20, 20, 20])
    # Обновляем экран
    p.display.update()
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if near([i, j]) not in (2, 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if near([i, j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2# Импорты
import time

import pygame as p
import random
from pygame.locals import *
import numpy as np

# Константы цветов RGB
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
# Создаем окно
root = p.display.set_mode((1000 , 500))
# 2х мерный список с помощью генераторных выражений
#cells = [[random.choice([0 , 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]

def choice(n):
    if n == 1:
        cells = np.zeros((25, 50))
        cells[10, 10:12] = 1
        cells[11, 10:12] = 1

    if n == 2:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 10:12] = 1
        cells[12, 9:11] = 1

    if n == 3:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 9] = 1
        cells[12, 9] = 1
        cells[13, 9] = 1
        cells[14, 9] = 1
        cells[15, 10] = 1

    if n == 4:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 10] = 1
        cells[12, 10] = 1

    if n == 5:
        cells = np.zeros((25, 50))
        cells[10, 10] = 1
        cells[11, 11] = 1
        cells[12, 9:12] = 1

    else:
        cells = [[random.choice([0, 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]

    return cells

cells = choice(1)


# Функция определения кол-ва соседей
def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count


# Основной цикл
while 1:
    # Заполняем экран белым цветом
    root.fill(WHITE)

    # Рисуем сетку
    for i in range(0 , root.get_height() // 20):
        p.draw.line(root , BLACK , (0 , i * 20) , (root.get_width() , i * 20))
    for j in range(0 , root.get_width() // 20):
        p.draw.line(root , BLACK , (j * 20 , 0) , (j * 20 , root.get_height()))
   # Нужно чтобы виндовс не думал что программа "не отвечает"
    for i in p.event.get():
        if i.type == QUIT:
            quit()
    # Проходимся по всем клеткам

    for i in range(0 , len(cells)):
        for j in range(0 , len(cells[i])):
            print(cells[i][j],i,j)
            p.draw.rect(root , (255 * cells[i][j] % 256 , 0 , 0) , [i * 20 , j * 20 , 20 , 20])
    # Обновляем экран
    p.display.update()
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if near([i , j]) not in (2 , 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if near([i , j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2