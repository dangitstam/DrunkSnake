__author__ = 'dangitstam'

# Maze Algorithm by Alex Onorati

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

screen_x = 800
screen_y = 600

red = (255, 0, 0)
blue = (0, 0, 255)

# r = 100
#
# sweg = []
#
table = pygame.image.load("/Users/dangitstam/Documents/Bar Table.png")

stool = pygame.image.load("/Users/dangitstam/Documents/Bar Stool.png")

#
# def frange(x, y, step):
#     while x < y:
#         yield x
#         x += step
#
# for x in frange(-200, 200, .5):
#     for y in frange(-200, 200, .5):
#         if int(round(x**2 + y**2)) == r**2:
#             sweg.append((x, y))
#
# sweg.append((0, r))
# sweg.append((r, 0))
# sweg.append((-r, 0))
# sweg.append((0, -r))
#
# print int(round(4.799999999 * 100))
#
# print sweg
# print len(sweg)

test_matrix = [[0 for x in range(15)] for y in range(20)]

re_maze = 0

def extend_maize(x, y):

    global re_maze

    test_matrix[x][y] = 1

    max = 2

    test = random.randint(0, max) >= 1

    if x + 1 < len(test_matrix) - 1 and test_matrix[x + 1][y] == 0 and is_near(x + 1, y) and test is True:
        extend_maize(x + 1, y)
        re_maze += 1

    test = random.randint(0, max) >= 1
    if x - 1 != 0 and test_matrix[x - 1][y] == 0 and is_near(x - 1, y) and test is True:
        extend_maize(x - 1, y)
        re_maze += 1

    test = random.randint(0, max) >= 1
    if y + 1 < len(test_matrix[0]) - 1 and test_matrix[x][y + 1] == 0 and is_near(x, y + 1) and test is True:
        extend_maize(x, y + 1)
        re_maze += 1

    test = random.randint(0, max) >= 1
    if y - 1 != 0 and test_matrix[x][y - 1] == 0 and is_near(x, y - 1) and test is True:
        extend_maize(x, y - 1)
        re_maze += 1


def maze_gen(x, y):
    extend_maize(x, y)
    if re_maze < 25:
        extend_maize(x, y)

def is_near(x, y):

    num_list = [0 for q in range(8)]
    num_list[0] = test_matrix[x - 1][y]
    num_list[1] = test_matrix[x - 1][y + 1]
    num_list[2] = test_matrix[x][y + 1]
    num_list[3] = test_matrix[x + 1][y + 1]
    num_list[4] = test_matrix[x + 1][y]
    num_list[5] = test_matrix[x + 1][y - 1]
    num_list[6] = test_matrix[x][y - 1]
    num_list[7] = test_matrix[x - 1][y - 1]

    test_1 = num_list[0] + num_list[1] + num_list[2] != 3
    test_2 = num_list[2] + num_list[3] + num_list[4] != 3
    test_3 = num_list[4] + num_list[5] + num_list[6] != 3
    test_4 = num_list[6] + num_list[7] + num_list[0] != 3

    return test_1 and test_2 and test_3 and test_4

place = random.randrange(0, 2)


def main():

    game_in = True
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.update()

    maze_gen(10, 10)

    print test_matrix

    while game_in:

        screen.fill(red)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_x:
                    game_in = False

        for j in range(0, len(test_matrix[0]) - 1):
            for i in range(0, len(test_matrix) - 1):
                if test_matrix[i][j] == 1:
                    pygame.draw.rect(screen, blue, [i * 50, j * 50, 40, 40])
                # if test_matrix[i][j] == 0:
                #     screen.blit(table, (i * 40, j * 40))

        pygame.draw.rect(screen, (0, 255, 0), [600, 0, 10, 600])

        #  if j > some table in a list.rect.x + self.radius....
        # recursion to blit tables?

        # circle_x = 300
        # circle_y = 257
        #
        # pygame.draw.circle(screen, blue, (circle_x, circle_y), 100)
        #
        # for coordinate in sweg:
        #     a = coordinate[0]
        #     b = coordinate[1]
        #     pygame.draw.circle(screen, (0, 255, 0), (int(round(a + circle_x)), int(round(b + circle_y))), 10)
        #
        # pygame.draw.circle(screen, (0, 0, 0), (400, 400), 27)
        # screen.blit(table, (400, 400))

        pygame.display.update()
        pygame.time.Clock().tick(30)

main()
