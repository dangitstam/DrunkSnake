__author__ = 'dangitstam'


# blit function credit to Blake from Nerdparadise

import pygame
import sys
import random
from pygame.locals import *

screen_x = 800
screen_y = 600

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Drunk Snake")

font1 = pygame.font.SysFont("Impact", 100)
font2 = pygame.font.SysFont("Impact", 30)
font3 = pygame.font.SysFont("Impact", 40)
font4 = pygame.font.SysFont("Impact", 18)
font5 = pygame.font.SysFont("Impact", 25)


def words(message, color, font_here):
    print_this = font_here.render(message, True, color)
    return print_this, print_this.get_rect()


def stuff_on_screen(message, color, x, y, font_here):
    textsurf, textrect = words(message, color, font_here)
    textrect.center = (x, y)
    screen.blit(textsurf, textrect)


def stuff_on_screen_corner(message, color, x, y, font_here):
    more_words = font_here.render(message, True, color)
    screen.blit(more_words, (x, y))

# Colors to be used throughout the game
drink = (0, 0, 0, 255)
beer = (241, 215, 68)
purple = (110, 47, 0)
green2 = (0, 255, 0)
green3 = (0, 200, 70)
coffee = (178, 143, 79)
iron = (130, 130, 130)
steel = (224, 223, 219)
mithril = (0, 76, 153)
adamant = (82, 139, 124)
rune = (104, 209, 255)
dragon = (180, 30, 30)
warning = (255, 30, 30)
white = (255, 255, 255)

mug = pygame.image.load(sys.path[0] + "/SnakeGameSprites/SnakebeerPIC.png")
mug2 = pygame.image.load(sys.path[0] + "/SnakeGameSprites/Snakebeer2.png")
snake_image_up = pygame.image.load(sys.path[0] + "/SnakeGameSprites/SnakeheadTOP.png")
snake_image_down = pygame.image.load(sys.path[0] + "/SnakeGameSprites/SnakeheadDOWN.png")
snake_image_right = pygame.image.load(sys.path[0] + "/SnakeGameSprites/Snakehead1.png")
coffee_pic = pygame.image.load(sys.path[0] + "/SnakeGameSprites/CoffeePic.png")
mice_pic = pygame.image.load(sys.path[0] + "/SnakeGameSprites/SnakeMice.png")
bar = pygame.image.load(sys.path[0] + "/SnakeGameSprites/Bar Stool.png")
bar_2 = pygame.image.load(sys.path[0] + "/SnakeGameSprites/Bar Table.png")

mice_image = pygame.transform.scale(mice_pic, (55, 55))

coffee_image = pygame.transform.scale(coffee_pic, (40, 40))

seat_pic = pygame.transform.scale(bar, (53, 70))

snake_size = 10

clock = pygame.time.Clock()

FPS = 40
buff_upgrade = 0
frame_count = 0
opacity_add = 0
opacity_minus = 0


opacity_counter = 0

coffee_thick = 26

health = 5

blood_alc = 0


def frange(x, y, step):
    while x < y:
        yield x
        x += step

mug_circle = []

for x in frange(-16, 16, .3):
    for y in frange(-16, 16, .3):
        if int(round(x**2 + y**2)) == 256:
            mug_circle.append((int(round(x)), int(round(y))))

mug_circle_filter = []

for item in mug_circle:
    if item not in mug_circle_filter:
        mug_circle_filter.append(item)

mug_circle_ = []
mug_circle_left = []
circle_coor = list()


def bar_obstacles(self):
    global circle_coor
    for x in frange(-100, 100, 5):
        for y in frange(-100, 100, 5):
            if int(round(x**2 + y**2)) == self.radius**2:
                circle_coor.append((x, y))


class Drinks(object):

    mug_spawn_x = random.randrange(50, screen_x - 50)
    mug_spawn_y = random.randrange(52, screen_x - 52)
    coffee_spawn_x = random.randrange(50, screen_x - 50)
    coffee_spawn_y = random.randrange(50, screen_y - 50)
    boost_points = 0
    drunk_points = 0
    alc_max = 5
    green = green3

    @staticmethod
    def beer_contact():
        Drinks.mug_spawn_x = random.randrange(10, screen_x - 32)
        Drinks.mug_spawn_y = random.randrange(10, screen_y - 32)
        return Drinks.mug_spawn_x, Drinks.mug_spawn_y

    @staticmethod
    def coffee_contact():
        Drinks.coffee_spawn_x = random.randrange(50, screen_x - 50)
        Drinks.coffee_spawn_y = random.randrange(50, screen_y - 50)
        return Drinks.coffee_spawn_x, Drinks.coffee_spawn_y

    @staticmethod
    def buff_stats(a, b, c, d):
        Drinks.boost_points += a
        Drinks.drunk_points += b
        Drinks.alc_max = c
        Drinks.green = d
        return Drinks.boost_points, Drinks.drunk_points, Drinks.alc_max, Drinks.green

    coffee_spawn = [coffee_spawn_x, coffee_spawn_y, coffee_thick, coffee_thick]


class Drunk(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mug
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-50, 50) + Drinks.mug_spawn_x
        self.rect.y = random.randint(-50, 50) + Drinks.mug_spawn_y

    def draw(self, where):
        where.blit(self.image, self.rect)

    def reset(self):
        self.rect.x = random.randint(-50, 50) + Drinks.mug_spawn_x
        self.rect.y = random.randint(-50, 50) + Drinks.mug_spawn_y

    def reset_big(self):
        self.rect.x = random.randint(-75, 75) + Drinks.mug_spawn_x
        self.rect.y = random.randint(-75, 75) + Drinks.mug_spawn_y


class Coffee(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = coffee_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, screen_x - 30)
        self.rect.y = random.randint(30, screen_y - 30)

    def reset(self):
        self.rect.x = random.randint(30, screen_x - 30)
        self.rect.y = random.randint(30, screen_y - 30)


class BarTable(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bar_2
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(200, screen_x - 200), random.randrange(200, screen_x - 200))
        self.radius = random.randrange(40, 100)

    def draw_table(self, place):
        place.blit(self.image, self.rect)

    def reset(self):
        self.radius = random.randrange(40, 100)
        self.rect.x = random.randrange(10, screen_x - 100)
        self.rect.y = random.randrange(10, screen_y - 100)


class BarStool(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bar
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 500)
        self.rect.y = random.randrange(100, 500)

    def draw(self, place):
        place.blit(self.image, self.rect)


class Buttons(object):

    def __init__(self, w, h, x, y, color_1, color_2, message):
        self.image = pygame.draw.rect(screen, color_1, [x, y, w, h])
        stuff_on_screen(message, color_2, w // 2 + x, h // 2 + y, font2)
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def start_menu_loop():

    menu = True

    menu_screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    def stuff_on_menu(message, color, x, y, font_here):
        textsurf, textrect = words(message, color, font_here)
        textrect.center = (x, y)
        menu_screen.blit(textsurf, textrect)

    while menu:

        menu_screen.fill(purple)
        stuff_on_menu("Drunk Snake", green3, screen_x / 2, screen_y / 2 - 200, font1)

        play = Buttons(300, 76, 250, 350, green3, white, "PLAY")
        quit = Buttons(300, 76, 250, 440, green3, white, "QUIT")

        menu_mouse_coor = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    menu = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.x < menu_mouse_coor[0] < play.x + play.w and play.y < menu_mouse_coor[1] < play.y + play.h:
                    menu = False
                elif quit.x < menu_mouse_coor[0] < quit.x + quit.w and quit.y < menu_mouse_coor[1] < quit.y + quit.h:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(FPS)


def snake_loop():

    resize_snake = pygame.transform.scale(snake_image_down, (34, 34))
    v = 0
    w = 0

    def snake(snake_list, snake_size):
        screen.blit(resize_snake, (snake_list[-1][0] + v, snake_list[-1][1] + w))
        for xny in snake_list[:-1]:
            pygame.draw.rect(screen, Drinks.green, [xny[0], xny[1], snake_size, snake_size])

    global green
    green = (0, 255, 0)

    head_x = screen_x / 2
    head_y = screen_y / 2

    buff_thicknesses = [10, 32]
    i = random.randrange(0, 2)
    global buff_thick
    buff_thick = buff_thicknesses[i]

    snake_list = []
    snake_length = 1

    global score
    score = 0

    global speed
    speed = 8

    game_out = False
    game_over = False
    global left_move, right_move, up_move, down_move
    left_move = False
    right_move = False
    up_move = False
    down_move = False
    # global speed_boost
    # speed_boost = 0

    mug_list = []
    coffee_list = []

    for i in range(2):
        add_coffee = Coffee()
        coffee_list.append(add_coffee)

    tables = []
    stools = []

    def add_bar_tables():
        for i in range(5):
            add_table = BarTable()
            add_table.radius = 100
            bar_obstacles(add_table)
            tables.append(add_table)
            for j in range(len(circle_coor)):
                add_stool = BarStool()
                add_stool.rect.x = circle_coor[j][0] + add_table.rect.x
                add_stool.rect.y = circle_coor[j][1] + add_table.rect.y
                stools.append(add_stool)

    add_bar_tables()

    # print(circle_coor)
    # print(stools)
    # print(tables)

    # for i in range(len(stools)):
    #     stools[i].draw(screen)
    #     print(stools[i].rect)
    #
    # for i in range(len(tables)):
    #     tables[i].draw_table(screen)

    def reset_attempt():
        for item in mug_list:
            if buff_thick == 10:
                item.reset()
            elif buff_thick == 32:
                item.reset_big()
        return mug_list

    while not game_out:

        """ blit Credit to NerdParadise """
        def blit_attempt(place, picture, coordinate, opacity):
            x = coordinate[0]
            y = coordinate[1]
            blit_try = pygame.Surface((picture.get_width(), picture.get_height())).convert()
            blit_try.blit(place, (-x, -y))
            blit_try.blit(picture, (0, 0))
            blit_try.set_alpha(opacity)
            place.blit(blit_try, coordinate)

        def flicker_words(message, place, coordinate, opacity, color, font_here):
            flicker = font_here.render(message, True, color)
            blit_attempt(place, flicker, coordinate, opacity)

        def blood_rush():
            global add_blur
            add_blur = Drunk()
            mug_list.append(add_blur)

        global frame_count
        global buff_upgrade
        global opacity_add
        global opacity_minus
        global mug_spin
        total_time = frame_count // FPS
        buff_seconds = total_time % 11
        buff_req = buff_upgrade // FPS
        buff_boost = buff_req % 1000
        opacity_count_test = opacity_add % 33
        mug_spin = (frame_count // 10) % 30

        if opacity_count_test <= 16:
            opacity_minus = 0
            opacity_counter = opacity_count_test
        elif opacity_count_test > 16:
            opacity_counter = opacity_count_test - (opacity_minus * 2)

        while game_over is True:
            screen.fill(purple)
            stuff_on_screen("GAME OVER", green3, screen_x / 2, screen_y / 2 - 125, font1)
            stuff_on_screen_corner("Score:", green3, 10, 10, font3)
            stuff_on_screen_corner(str(score), green3, 125, 13, font3)
            play_again = Buttons(300, 76, 250, 350, green3, white, "PLAY AGAIN")
            quit_again = Buttons(300, 76, 250, 440, green3, white, "QUIT")
            pygame.display.update()

            global mouse_coor
            mouse_coor = pygame.mouse.get_pos()

            for event in pygame.event.get():
                global health
                if event.type == pygame.QUIT:
                    game_over = False
                    game_out = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_out = True
                        game_over = False
                    if event.key == pygame.K_x:
                        health = 5
                        snake_loop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again.x < mouse_coor[0] < play_again.x + play_again.w:
                        if play_again.y < mouse_coor[1] < play_again.y + play_again.h:
                            health = 5
                            snake_loop()
                    if quit_again.x < mouse_coor[0] < quit_again.x + quit_again.w:
                        if quit_again.y < mouse_coor[1] < quit_again. y + quit_again.h:
                            pygame.quit()
                            sys.exit()

        # Handles direction changes
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            #     left_move = event.key == pygame.K_LEFT and right_move is False
            #     right_move = event.key == pygame.K_RIGHT and left_move is False
            #     up_move = event.key == pygame.K_UP and down_move is False
            #     down_move = event.key == pygame.K_DOWN and up_move is False
                if event.key == pygame.K_LEFT and right_move is False:
                    left_move = True
                    right_move = False
                    up_move = False
                    down_move = False
                elif event.key == pygame.K_RIGHT and left_move is False:
                    left_move = False
                    right_move = True
                    up_move = False
                    down_move = False
                elif event.key == pygame.K_DOWN and up_move is False:
                    left_move = False
                    right_move = False
                    up_move = False
                    down_move = True
                elif event.key == pygame.K_UP and down_move is False:
                    left_move = False
                    right_move = False
                    up_move = True
                    down_move = False
                # elif event.key == pygame.K_SPACE:
                #     speed_boost = 7
                #     pygame.key.set_repeat(1, 10)
                # elif event.type == pygame.KEYUP:
                #     if event.key == pygame.K_SPACE:
                #         speed_boost = 0

        # Changes the direction of movement and orientation of the snake's head
        # based on player input with arrow keys.
        if left_move is True:
            v = - 20
            w = - 2
            resize_snake = pygame.transform.scale(pygame.transform.flip(snake_image_right, True, False), (34, 34))
            head_x -= speed
        elif right_move is True:
            v = + 3
            w = - 2
            resize_snake = pygame.transform.scale(snake_image_right, (34, 34))
            head_x += speed
        elif down_move is True:
            v = - 4
            w = 0
            resize_snake = pygame.transform.scale(snake_image_down, (31, 31))
            head_y += speed
        elif up_move is True:
            v = - 11
            w = - 20
            resize_snake = pygame.transform.scale(snake_image_up, (34, 34))
            head_y -= speed

        # Randomizes movement based on current blood alcohol level.
        global blood_alc
        if blood_alc > 0:
            if left_move or right_move is True:
                head_y += random.randrange(-blood_alc, blood_alc)
            elif up_move or down_move is True:
                head_x += random.randrange(-blood_alc, blood_alc)

        if blood_alc > Drinks.alc_max:
            speed -= blood_alc - Drinks.alc_max

        if head_x >= screen_x:
            health -= 1
            head_x -= 20
            right_move = False
            if head_y < screen_y // 2:
                down_move = True
            else:
                up_move = True
        elif head_x <= 0:
            health -= 1
            head_x += 20
            left_move = False
            if head_y < screen_y // 2:
                down_move = True
            else:
                up_move = True
        elif head_y >= screen_y:
            health -= 1
            head_y -= 20
            down_move = False
            if head_x < screen_x // 2:
                right_move = True
            else:
                left_move = True
        elif head_y <= 0:
            health -= 1
            head_y += 20
            up_move = False
            if head_x < screen_x // 2:
                right_move = True
            else:
                left_move = True

        # UI for meters, score, and colors
        screen.fill(purple)
        alc_meter_length = screen_x * .7 * blood_alc / Drinks.alc_max
        stuff_on_screen_corner("Score:", green2, 10, 540, font3)
        stuff_on_screen_corner(str(score), green2, 125, 540, font3)
        stuff_on_screen_corner("B. A. C", green3, 15, 10, font3)
        stuff_on_screen_corner(str(float(blood_alc) / 100), green3, alc_meter_length + 137, 50, font4)
        stuff_on_screen_corner("Health:", green3, 15, 60, font3)

        # Flicker system warns player when blood alcohol level is near toxic
        warning_flicker = random.randrange(100, 255)

        if blood_alc < Drinks.alc_max - 1:
            lethal_flicker = 255
        elif blood_alc >= Drinks.alc_max - 1:
            lethal_flicker = warning_flicker

        pygame.draw.rect(screen, beer, [150, 20, screen_x * .7, 30])
        pygame.draw.rect(screen, dragon, [150, 20, alc_meter_length, 30])
        flicker_words("Maximum", screen, (660, 50), lethal_flicker, warning, font5)
        flicker_words("B.A.C", screen, (685, 75), lethal_flicker, warning, font5)

        overdose = False

        if blood_alc > Drinks.alc_max:
            overdose = True

        for i in range(health):
            health_mug = pygame.transform.scale(mug, (110, 110))
            screen.blit(health_mug, (i * 50 - 10, 80))

        if health == 0:
            game_over = True

        Drinks.buff_stats(0, 0, 8, green3)

        mug_opac = 55 + opacity_counter * 13

        def draw_instance():
            for instance in mug_list:
                mug_coordinates = (instance.rect.x, instance.rect.y + opacity_counter)
                if buff_thick == 10:
                    instance.image = mug2
                    if instance.rect.x < 0 or instance.rect.x > screen_x - 19\
                            or instance.rect.y < 0 or instance.rect.y > screen_y - 20:
                        instance.reset()
                    blit_attempt(screen, instance.image, mug_coordinates, mug_opac)
                elif buff_thick == 32:
                    instance.image = mug
                    if instance.rect.x < 0 or instance.rect.x > screen_x - 50:
                        instance.reset()
                    if instance.rect.y < 0 or instance.rect.y > screen_y - 52:
                        instance.reset()
                        instance.rect.y = 2 * screen_y - instance.rect.y
                    blit_attempt(screen, instance.image, mug_coordinates, mug_opac)

        draw_instance()

        if blood_alc >= Drinks.alc_max - 2:
            for shot in coffee_list:
                coffee_coordinates = (shot.rect.x, shot.rect.y - int(round(opacity_counter * .5)))
                screen.blit(shot.image, coffee_coordinates)
                if abs(head_x - shot.rect.x) < 26 or abs(shot.rect.x - head_x) < 10:
                    if abs(head_y - shot.rect.y) < 26 or abs(shot.rect.y - head_y) < 10:
                        blood_alc -= 1
                        shot.reset()

        snake_head = list()
        snake_head.append(head_x)
        snake_head.append(head_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_over = True

        for i in range(0, len(snake_list) - 5):
            if abs(snake_list[i][0] - head_x) < 9:
                if abs(snake_list[i][1] - head_y) < 9:
                    game_over = True

        snake(snake_list, snake_size)

        if len(mug_list) > blood_alc:
            del mug_list[0]

        stats_on = False
        y_bounce = Drinks.mug_spawn_y + opacity_counter

        if buff_thick == 10:
            blit_attempt(screen, mug2, (Drinks.mug_spawn_x - 9, y_bounce - 10), mug_opac)
            for i in range(-1, len(mug_list) - 1):
                if abs(mug_list[i].rect.x - head_x + 9) < 10:
                    if abs(mug_list[i].rect.y - head_y + 10) < 10:
                        if opacity_add % 2 == 0:
                            mug_list[i].rect.x += 7
                        else:
                            mug_list[i].rect.x -= 7
            if abs(Drinks.mug_spawn_x - head_x) < 10:
                if abs(Drinks.mug_spawn_y - head_y) < 10:
                    stats_on = True
        elif buff_thick == 32:
            if blood_alc >= 0:
                blit_attempt(screen, mug, (Drinks.mug_spawn_x - 18, y_bounce - 20), mug_opac)
            for i in range(-1, len(mug_list) - 1):
                if abs(head_x - mug_list[i].rect.x - 18) < 31 or abs(mug_list[i].rect.x - head_x + 18) < 9:
                    if abs(head_y - mug_list[i].rect.y - 20) < 31 or abs(mug_list[i].rect.y - head_y + 20) < 9:
                        if opacity_add % 2 == 0:
                            mug_list[i].rect.x += 7
                        else:
                            mug_list[i].rect.x -= 7
            if abs(Drinks.mug_spawn_x + 18 - head_x) < 31:
                if abs(Drinks.mug_spawn_y + 20 - head_y) < 31:
                    stats_on = True

        pygame.display.update()

        if stats_on is True:
            i = random.randrange(0, 2)
            blood_rush()
            snake_length += 1
            score += 1
            buff_thick = buff_thicknesses[i]
            Drinks.beer_contact()
            reset_attempt()
            frame_count = 0
            blood_alc += 1
            if overdose is True:
                health -= 1
            if blood_alc > Drinks.alc_max:
                score -= 2

        opacity_minus += 1
        frame_count += 1
        buff_upgrade += 1
        opacity_add += 1
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

start_menu_loop()
snake_loop()
