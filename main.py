import pygame
import sys
import math
from pygame.locals import *


class Ball:
    def __init__(self, v):
        self.x = 200
        self.y = 600
        self.vx = v[0]
        self.vy = v[1]
        self.distance = 700

    def get_pos(self, t):
        return self.x + self.vx * t, self.y - self.vy * t + 490 * t * t

    def run_animation(self):
        time = 0
        animation_clock = pygame.time.Clock()

        total_time2 = self.vy / 490
        if self.vx == 0:
            total_time = total_time2
        else:
            total_time = min(self.distance / self.vx, total_time2)

        while time <= total_time:
            dt = animation_clock.tick(FPS) / 1000
            time += dt
            self.animate(time)

    def animate(self, t):
        new_screen = pygame.Surface((SCREENX, SCREENY))
        new_screen.blit(EMPTY_BOARD, (0, 0))
        pygame.draw.arc(new_screen, RED, Rect(700, 200, 200, 150), 0, math.pi, 10)
        ballx, bally = self.get_pos(t)
        new_screen.blit(BALL, (ballx, bally))
        pygame.draw.arc(new_screen, RED, Rect(700, 200, 200, 150), math.pi, math.tau, 10)
        DISPLAYSURF.blit(new_screen, (0, 0))
        pygame.display.update()


pygame.init()

SCREENX = 1000
SCREENY = 800

DISPLAYSURF = pygame.display.set_mode((SCREENX, SCREENY))
GREEN = (52, 235, 103)
RED = (196, 26, 14)
DISPLAYSURF.fill(GREEN)

EMPTY_COLOR = (100, 100, 100)
EMPTY_BOARD = pygame.Surface((SCREENX, SCREENY))
EMPTY_BOARD.fill((100, 100, 100))

BALL_DIAMETER = 100
BALL_COLOR = (219, 116, 20)
BALL = pygame.Surface((BALL_DIAMETER, BALL_DIAMETER))
BALL.fill(EMPTY_COLOR)
pygame.draw.circle(BALL, BALL_COLOR, (BALL_DIAMETER // 2, BALL_DIAMETER // 2), BALL_DIAMETER // 2)

LAUNCH_SCALE = 10

pygame.init()
FPS = 60
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
levels = font_MED.render("LEVELS", True, textColor[1])
main = font_MED.render("MAIN MENU", True, textColor[1])
tit_lvl = font_LARGE.render("LEVELS", True, textColor[3])
tit_tut = font_LARGE.render("HOW TO PLAY", True, textColor[3])
back = font_MED.render("BACK", True, textColor[1])
tit_1 = pygame.image.load("basketball.png")
tit_2 = pygame.image.load("physics.png")
mouse_1 = pygame.image.load("mouser123.png")
mouse_2 = pygame.image.load("mouser.png")
img_1 = pygame.image.load("shooter.png")
img_1 = pygame.transform.scale(img_1, (330, 330))
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
    DISPLAYSURF.blit(BALL, (200, 600))
    pygame.draw.arc(DISPLAYSURF, RED, Rect(700, 200, 200, 150), 0, math.tau, 10)


def launch(poss):
    ball = Ball((LAUNCH_SCALE * (250 - poss[0]), LAUNCH_SCALE * (poss[1] - 650)))
    ball.run_animation()


def draw_line(poss):
    pygame.draw.line(DISPLAYSURF, GREEN, (250, 650), (poss[0], poss[1]), 1)


pygame.mouse.set_visible(False)
while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            a = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        if event.type == MOUSEBUTTONDOWN:
            distance = math.sqrt(math.pow(pos[0] - 700, 2) +
                                 math.pow(pos[1] - 580, 2))
            distance2 = math.sqrt(math.pow(pos[0] - 250, 2) +
                                  math.pow(pos[1] - 650, 2))
            if in_main and distance < 100:
                play()
                in_main = False
            if not in_main and distance2 < 50:
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
    time_passed = gameClock.tick(30)
    time_milis += time_passed
    pygame.display.update()
