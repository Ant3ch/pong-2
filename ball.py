import pygame
from config import *
import random
import math

score1_ball = 0
score2_ball = 0
class ball:
    def __init__(self):
        self.size = (50, 50)
        self.rect = pygame.Rect((0, 0), self.size)
        self.speedx = 3
        self.speedy = 3
        self.current_time = 0

    def draw(self):
        pygame.draw.ellipse(win, WHITE, self.rect)
        self.current_time = pygame.time.get_ticks()

    def move(self):
        global score1_ball,score2_ball
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # bouncing
        if self.rect.x <= 0:
            self.rect.center = WIDTH / 2, HEIGHT / 2
            self.speedy *= random.choice([1, -1])
            self.speedx *= random.choice([1, -1])
            # score player 2
            score2_ball+=1





        elif self.rect.x >= WIDTH:
            self.rect.center = WIDTH / 2, HEIGHT / 2
            self.speedy *= random.choice([1, -1])
            self.speedx *= random.choice([1, -1])
            # score player 1
            score1_ball+=1

        elif self.rect.y <= 0:
            self.speedy *= -1

        elif self.rect.y >= HEIGHT - self.size[1]:
            self.speedy *= -1
