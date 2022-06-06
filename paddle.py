from pygame.locals import *
import pygame
import config
from config import *


class player:
    def __init__(self, x, y):

        self.size = (10, 140)
        self.rect = pygame.Rect((0, 0), self.size)
        self.rect.center = (x, y)
        self.speed = 3
        self.keys = [eval(f"K_{key_up}"),eval(f"K_{key_down}"),eval(f"K_{key_left}"),eval(f"K_{key_right}")]
        self.player1 = False
        self.player2 = False





    def draw(self):

        pygame.draw.rect(config.win, config.WHITE, self.rect)

    def moves(self):
        key = pygame.key.get_pressed()
        key2 = pygame.key.get_pressed()
        rect = self.rect
        speed = self.speed
        size = self.size

        # UP
        if key[self.keys[0]]:
            rect.y -= speed


        # DOWN
        elif key[self.keys[1]]:
            rect.y += speed
        # RIGHT
        elif key[self.keys[3]]:
            rect.x += speed
        # LEFT
        elif key[self.keys[2]]:

            rect.x -= speed

        # diagonal right up add

        if key[self.keys[0]] and key2[self.keys[3]]:
            rect.y -= speed - speed  # because it's added two times with key
            rect.x += speed # because idk it's removed

        # diagonal left down
        if key[self.keys[1]] and key2[self.keys[2]]:
            rect.y += speed - speed
            rect.x -= speed
        # diagonal right down
        if key[self.keys[1]] and key2[self.keys[3]]:
            rect.x += speed
            rect.y -= speed - speed
        # diagonal left up
        if key[self.keys[0]] and key2[self.keys[2]]:
            rect.x -= speed
            rect.y += speed - speed

        # constraint

        if rect.x <= 0:
            rect.x = 0
        elif rect.x >= WIDTH - 10:
            rect.x = WIDTH- 10
        elif rect.y <= 0:
            rect.y = 0
        elif rect.y >= HEIGHT - size[1]:
            rect.y = HEIGHT - size[1]

        # middle line
        if self.player1:
            if rect.right >= WIDTH / 2:
                rect.right = WIDTH / 2
        elif self.player2:
            if rect.left <= WIDTH / 2:
                rect.left = WIDTH / 2


