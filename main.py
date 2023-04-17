import math
import sys, pygame
from pygame.locals import *


class Ball:
    def __init__(self, v):
        self.x = 200
        self.y = 600
        self.vx = v[0]
        self.vy = v[1]
        self.distance = 600

    def get_pos(self, t):
        return self.x + self.vx * t, self.y - self.vy * t + 490 * t * t

    def run_animation(self):
        time = 0
        animation_clock = pygame.time.Clock()

        # total_time = self.distance / self.vx
        total_time = self.vy / 490

        while time <= total_time:
            dt = animation_clock.tick() / 1000
            time += dt
            self.animate(time)

        print(self.get_pos(total_time))

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


def main():
    ball = Ball((450, 900))
    ball.run_animation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    main()
