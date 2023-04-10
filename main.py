import pygame
import sys
from pygame.locals import *

pygame.init()
FPS = 30
gameClock = pygame.time.Clock()
up = False
down = False
surface = pygame.display.set_mode((1000, 800))
font_LARGE = pygame.font.Font("freesansbold.ttf", 100)
textColor = ((119, 110, 101), (249, 246, 242), (200, 242, 100), (52, 235, 113))
title = font_LARGE.render("BASKETBALL", True, textColor[3])
font_MED = pygame.font.Font("freesansbold.ttf", 40)
font_SMALL = pygame.font.Font("freesansbold.ttf", 30)
play = font_MED.render("PLAY", True, textColor[1])
next_level = font_MED.render("NEXT LVL", True, textColor[1])
levels = font_MED.render("LEVELS", True, textColor[1])
main = font_MED.render("MAIN MENU", True, textColor[1])
tut = font_SMALL.render("HOW TO PLAY", True, textColor[1])
tit_lvl = font_LARGE.render("LEVELS", True, textColor[3])
tit_tut = font_LARGE.render("HOW TO PLAY", True, textColor[3])
dos = font_LARGE.render("2", True, textColor[1])
uno = font_LARGE.render("1", True, textColor[1])
back = font_MED.render("BACK", True, textColor[1])
rule_1 = font_MED.render("- 1", True, textColor[1])
rule_2 = font_MED.render("- 2", True, textColor[1])
rule_3 = font_MED.render("- 3", True, textColor[1])
rule_4 = font_MED.render("- 4", True, textColor[1])
tit_1 = pygame.image.load("basketball.png")
tit_2 = pygame.image.load("physics.png")
tit_2 = pygame.transform.scale(tit_2, (240, 64))
tit_1 = pygame.transform.scale(tit_1, (300, 64))
time_milis = 0

surface.fill((0, 255, 0))
surface.blit(tit_1, (100, 100))
surface.blit(tit_2, (100, 200))

while True:
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
        if event.type == KEYDOWN:
            a = pygame.key.get_pressed()
            if a[K_UP]:
                up = True
            if a[K_DOWN]:
                down = True
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
    time_passed = gameClock.tick(30)
    time_milis += time_passed
    pygame.display.update()
