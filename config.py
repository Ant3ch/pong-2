import pygame
from pygame.locals import *
# white,black


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# pygame conf
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1280, 720
FPS = 144
SYS_FONT = "Comic Sans MS"

clock = pygame.time.Clock()
caption = "Ping Pong 2"
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(caption)

# different font size
H0 = pygame.font.SysFont(SYS_FONT, 55)
H1 = pygame.font.SysFont(SYS_FONT, 32)
H2 = pygame.font.SysFont(SYS_FONT, 24)
H3 = pygame.font.SysFont(SYS_FONT, 18)
H4 = pygame.font.SysFont(SYS_FONT, 16)
H5 = pygame.font.SysFont(SYS_FONT, 13)
H6 = pygame.font.SysFont(SYS_FONT, 10)


# player 1 - keys
key_up = "z"
key_left = "q"  # letters have to be lowercase
key_down = "s"
key_right = "d"

# player 2 - keys

player2_key_up = "UP"
player2_key_left = "LEFT"  # Arrows keys and special keys like space have to be uppercase
player2_key_down = "DOWN"
player2_key_right = "RIGHT"




