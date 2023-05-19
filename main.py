import math
import pygame
import sys

from pygame.locals import *


class Ball:
    def __init__(self, v):
        self.x0 = BALLX
        self.y0 = BALLY
        self.vx = v[0]
        self.vy = v[1]

    def get_pos(self, t):
        return self.x0 + self.vx * t, self.y0 + self.vy * t + 490 * t * t

    def get_velo(self, t):
        return self.vx, self.vy + 980 * t

    def run_animation(self, n, board):
        t = 0
        animation_clock = pygame.time.Clock()

        time_to_ground = (- self.vy + math.sqrt(self.vy ** 2 + 1960 * (SCREENY - self.y0))) / 980
        time_to_left = (- self.x0) / self.vx
        time_to_right = (SCREENX - self.x0) / self.vx

        times = [time_to_ground, time_to_left, time_to_right]

        for time in times:
            if time <= 0:
                times.remove(time)

        time = min(times)

        if True:
            for i in range(math.floor(time * 1000)):
                x, y = self.get_pos(i / 1000)
                dx = x - FRONT_RIM
                dy = y - HOOP_Y_CENTER
                dist = math.sqrt(dx ** 2 + dy ** 2)
                if dist <= BALL_RADIUS + 5 and i > 50:
                    total_time = i / 1000
                    while t <= total_time:
                        dt = animation_clock.tick() / 1000
                        t += dt * 1.2
                        animate(self.get_pos(t))
                    self.x0, self.y0 = (x, y)
                    vx, vy = self.get_velo(total_time)
                    m = - (dx * vx + dy * vy) / (dx ** 2 + dy ** 2)
                    self.vx = (vx + 2 * m * dx) / 2
                    self.vy = (vy + 2 * m * dy) / 2

                    return self.run_animation(n + 1, True)

        t_height1 = (FRONT_RIM + BALL_RADIUS - self.x0) / self.vx
        t_height2 = (FRONT_RIM + HOOP_WIDTH - BALL_RADIUS - self.x0) / self.vx
        y1 = self.get_pos(t_height1)[1]
        y2 = self.get_pos(t_height2)[1]
        made = y1 <= HOOP_Y_CENTER <= y2 or y2 <= HOOP_Y_CENTER <= y1

        if HOOP_Y_CENTER - BACK_BOARD_HEIGHT <= y2 <= HOOP_Y_CENTER and t_height2 > 0 and board:
            total_time = t_height2
            while t <= total_time:
                dt = animation_clock.tick() / 1000
                t += dt * 1.2
                animate(self.get_pos(t))
            self.x0, self.y0 = self.get_pos(total_time)
            self.vx = -self.vx / 4
            self.vy = self.get_velo(total_time)[1] / 4
            return self.run_animation(n + 1, False)

        while t <= time:
            dt = animation_clock.tick() / 1000
            t += dt * 1.2
            animate(self.get_pos(t))
        return made


def animate(poss):
    new_screen = pygame.Surface((SCREENX, SCREENY))
    new_screen.blit(EMPTY_BOARD, (0, 0))
    pygame.draw.arc(new_screen, RED, HOOP, 0, math.pi, 10)
    ballx, bally = poss
    new_screen.blit(BALL, (ballx - 50, bally - 50))
    pygame.draw.arc(new_screen, RED, HOOP, math.pi, math.tau, 10)
    if green:
        pygame.draw.line(new_screen, GREEN, (900, HOOP_Y_CENTER), (900, HOOP_Y_CENTER - BACK_BOARD_HEIGHT), 10)
    else:
        pygame.draw.line(new_screen, WHITE, (900, HOOP_Y_CENTER), (900, HOOP_Y_CENTER - BACK_BOARD_HEIGHT), 10)
    new_screen.blit(score, (30, 30))
    new_screen.blit(record, (260, 30))
    num = font_MED.render(str(current), True, textColor[1])
    new_screen.blit(num, (90, 80))
    numba = font_MED.render(str(best), True, textColor[1])
    new_screen.blit(numba, (290, 80))
    new_screen.blit(harden2, (0, 487))
    DISPLAYSURF.blit(new_screen, (0, 0))
    pygame.display.update()


best = 0
current = 0
green = False
seconds_green = 0


pygame.init()

SCREENX = 1000
SCREENY = 800

DISPLAYSURF = pygame.display.set_mode((SCREENX, SCREENY))
GREEN = (52, 235, 103)
RED = (196, 26, 14)
WHITE = (255, 255, 255)

DISPLAYSURF.fill(GREEN)

EMPTY_COLOR = (100, 100, 100)
TRANSPARENT_EMPTY = (100, 100, 100, 0)
EMPTY_BOARD = pygame.Surface((SCREENX, SCREENY))
EMPTY_BOARD.fill((100, 100, 100))

BALL_DIAMETER = 100
BALL_RADIUS = BALL_DIAMETER // 2
BALL_COLOR = (219, 116, 20)
BALL = pygame.Surface((BALL_DIAMETER, BALL_DIAMETER)).convert_alpha()
BALL.fill(TRANSPARENT_EMPTY)

BALLX = 200
BALLY = 550

pygame.draw.circle(BALL, BALL_COLOR, (BALL_DIAMETER // 2, BALL_DIAMETER // 2), BALL_DIAMETER // 2)

LAUNCH_SCALE = 10

HOOP_HEIGHT = 150
HOOP_SMAXIS = 75
HOOP_WIDTH = 200
FRONT_RIM = 700
HOOP_Y_CENTER = HOOP_HEIGHT + HOOP_SMAXIS

HOOP = Rect(FRONT_RIM, HOOP_HEIGHT, HOOP_WIDTH, HOOP_SMAXIS * 2)

BACK_BOARD_HEIGHT = 200

pygame.init()
FPS = 120
gameClock = pygame.time.Clock()
up = False
down = False
screen_x = 1000
screen_y = 800
DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y))
font_LARGE = pygame.font.Font("freesansbold.ttf", 100)
textColor = ((119, 110, 101), (249, 246, 242), (200, 242, 100), (52, 235, 113))
title = font_LARGE.render("BASKETBALL", True, textColor[3])
font_MED = pygame.font.Font("freesansbold.ttf", 40)
font_SMALL = pygame.font.Font("freesansbold.ttf", 30)
playa = font_MED.render("PLAY", True, textColor[1])
score = font_MED.render("SCORE", True, textColor[1])
record = font_MED.render("BEST", True, textColor[1])
main = font_MED.render("MENU", True, textColor[1])
tit_lvl = font_LARGE.render("LEVELS", True, textColor[3])
tit_tut = font_LARGE.render("HOW TO PLAY", True, textColor[3])
back = font_MED.render("BACK", True, textColor[1])
tit_1 = pygame.image.load("basketball.png")
tit_2 = pygame.image.load("physics.png")
mouse_1 = pygame.image.load("mouser123.png")
mouse_2 = pygame.image.load("mouser.png")
img_1 = pygame.image.load("shooter.png")
harden = pygame.image.load("harden.png")
harden2 = pygame.image.load("harden2.png")
harden2 = pygame.transform.scale(harden2, (330, 330))
img_1 = pygame.transform.scale(img_1, (330, 330))
harden = pygame.transform.scale(harden, (330, 330))
mouse_2 = pygame.transform.scale(mouse_2, (30, 30))
mouse_1 = pygame.transform.scale(mouse_1, (30, 30))
tit_2 = pygame.transform.scale(tit_2, (350, 80))
tit_1 = pygame.transform.scale(tit_1, (600, 64))
time_milis = 0
left_click = False
in_main = True
pulling = False


def menu():
    DISPLAYSURF.fill((96, 215, 230))
    DISPLAYSURF.blit(tit_1, (150, 80))
    DISPLAYSURF.blit(tit_2, (450, 150))
    DISPLAYSURF.blit(img_1, (-50, 180))
    pygame.draw.circle(DISPLAYSURF, (230, 124, 18), (700, 580), 100)
    DISPLAYSURF.blit(playa, (700 - playa.get_width() // 2, 580 - playa.get_height() // 2))
    return


def play():
    DISPLAYSURF.fill((100, 100, 100))
    pygame.draw.arc(DISPLAYSURF, RED, HOOP, 0, math.tau, 10)
    if green:
        pygame.draw.line(DISPLAYSURF, GREEN, (900, HOOP_Y_CENTER), (900, HOOP_Y_CENTER - BACK_BOARD_HEIGHT), 10)
    else:
        pygame.draw.line(DISPLAYSURF, WHITE, (900, HOOP_Y_CENTER), (900, HOOP_Y_CENTER - BACK_BOARD_HEIGHT), 10)
    DISPLAYSURF.blit(score, (30, 30))
    DISPLAYSURF.blit(record, (260, 30))
    num = font_MED.render(str(current), True, textColor[1])
    DISPLAYSURF.blit(num, (90, 80))
    numba = font_MED.render(str(best), True, textColor[1])
    DISPLAYSURF.blit(numba, (290, 80))
    DISPLAYSURF.blit(harden, (55, 487))



def make():
    global current, best, green
    current += 1
    if current > best:
        best = current
    green = True
    return


def miss():
    global current, best, green
    green = False
    if current > best:
        best = current
    current = 0
    return


def launch(poss):
    ball = Ball((LAUNCH_SCALE * (BALLX - poss[0]), LAUNCH_SCALE * (BALLY - poss[1])))
    made = ball.run_animation(1, True)
    if made:
        make()
    else:
        miss()


def draw_line(poss):
    pygame.draw.line(DISPLAYSURF, GREEN, (BALLX, BALLY), (poss[0], poss[1]), 1)


pygame.mouse.set_visible(False)

time_passed = 0

while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        if event.type == MOUSEBUTTONDOWN:
            distance = math.sqrt(math.pow(pos[0] - 700, 2) +
                                 math.pow(pos[1] - 580, 2))
            distance2 = math.sqrt(math.pow(pos[0] - BALLX, 2) +
                                  math.pow(pos[1] - BALLY, 2))
            if in_main and distance < 100:
                play()
                in_main = False
            if not in_main and distance2 < BALL_RADIUS:
                pulling = True
        if event.type == MOUSEBUTTONUP and pulling:
            pulling = False
            launch(pos)
        if event.type == MOUSEMOTION and pulling:
            play()
            draw_line(pos)
        if not in_main and not pulling:
            play()
        if in_main:
            menu()
        if mouse_state[0]:
            DISPLAYSURF.blit(mouse_1, (pos[0] - 15, pos[1] - 15))
        else:
            DISPLAYSURF.blit(mouse_2, (pos[0] - 15, pos[1] - 15))

    time_milis += time_passed
    pygame.display.update()
