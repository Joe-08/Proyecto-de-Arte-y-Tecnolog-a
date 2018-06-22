#El juego de la vida

import pygame
import sys
import time

LENGTH = 1000   #Cambias el ancho y largo de la ventana
N = 60 #numero de cuadrados N x N

SIDE = LENGTH / N
BOX = SIDE * 0.8
SPACE = (SIDE - BOX) / 2
DARK = (15, 15, 15)
BLUE = (15, 109, 181)
patron_minas = []
temp = []


def main():
    pygame.init()
    screen = pygame.display.set_mode((LENGTH, LENGTH))
    pygame.display.set_caption('Juego de la vida de Conway')

    for posicion_fila in range(N):
        patron_minas.append([])
        for posicion_columna in range(N):
            patron_minas[-1].append(False)
            draw_box(screen, posicion_fila, posicion_columna, DARK)

    conway_game(screen)


def add_box(screen, x, y):
    global SPACE, SIDE, BOX, GREY, patron_minas

    if patron_minas[y][x]:
        patron_minas[y][x] = False
        draw_box(screen, x, y, DARK)
    else:
        patron_minas[y][x] = True
        draw_box(screen, x, y, BLUE)


def draw_box(screen, x, y, color):
    global SPACE, SIDE, BOX

    pygame.draw.rect(screen, color,
                     [SPACE + SIDE * x, SPACE + SIDE * y,
                      BOX, BOX])
    pygame.display.update()


def conway_game(screen):

    start = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 112:
                    start = True
                elif event.key == 114:
                    start = False

        if start:
            conway_run(screen)
        else:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x = int(x // SIDE)
                y = int(y // SIDE)
                add_box(screen, x, y)
                time.sleep(0.3)


def conway_run(screen):
    global N, DARK, GREY, patron_minas, temp

    temp = []

    for i in patron_minas:
        temp.append([])
        for j in i:
            temp[-1].append(j)

    for posicion_fila in range(N):
        for posicion_columna in range(N):
            box = temp[posicion_fila][posicion_columna]
            life = count_box(posicion_fila, posicion_columna, box)
            if box:
                if life - 1 != 2 and life - 1 != 3:
                    patron_minas[posicion_fila][posicion_columna] = False
                    draw_box(screen, posicion_columna, posicion_fila, DARK)
            else:
                if life == 3:
                    patron_minas[posicion_fila][posicion_columna] = True
                    draw_box(screen, posicion_columna, posicion_fila, BLUE)
    time.sleep(0.3)


def count_box(posicion_fila, posicion_columna, box):
    global temp

    a, b, c, d, n = 0, 0, 0, 0, 0

    if posicion_fila == 0:
        a = 1
    if posicion_fila == len(temp) - 1:
        b = 1
    if posicion_columna == 0:
        c = 1
    if posicion_columna == len(temp[0]) - 1:
        d = 1
    for i in range(-1 + a, 2 - b):
        for j in range(-1 + c, 2 - d):
            n += temp[posicion_fila + i][posicion_columna + j]
    return n

if __name__ == "__main__":
    main()