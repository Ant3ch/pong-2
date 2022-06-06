from pygame.locals import *
import pygame
from config import *
import paddle
import ball
import math

# player1-2 instances
Paddle_player1 = paddle.player(50, HEIGHT / 2)
Paddle_player2 = paddle.player(WIDTH - 50, HEIGHT / 2)

# player 2 keys
Paddle_player2.keys = [eval(f"K_{player2_key_up}"), eval(f"K_{player2_key_down}"), eval(f"K_{player2_key_left}"),
                       eval(f"K_{player2_key_right}")]

# ball instance
Ball = ball.ball()
Ball.rect.center = (WIDTH / 2, HEIGHT / 2)

# we tell to our proggramme wich player is wich player
Paddle_player1.player1 = True
Paddle_player2.player2 = True


class Main_game():
    def __init__(self):
        self.state = "Main"
        self.running = True

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                quit()
        # verify collision player 1 and Two
        if Paddle_player1.rect.colliderect(Ball.rect) or Paddle_player2.rect.colliderect(Ball.rect):
            if Ball.speedx < 0:
                Ball.rect.x += 20
                Ball.speedy = Ball.speedy # here we want to get our speed like -3,-3 and not -3, 3 etc...
                Ball.speedx = -Ball.speedx


            elif Ball.speedx > 0:
                Ball.rect.x -= 20 # just few gap...

                Ball.speedy = Ball.speedy
                Ball.speedx = -Ball.speedx

        # visual

        win.fill(BLACK)
        Paddle_player1.moves()
        Paddle_player2.moves()
        Ball.move()

        Paddle_player1.draw()
        Paddle_player2.draw()
        Ball.draw()
        self.draw_score()

    def controller(self):
        if self.state == "Main":
            self.main()

    def draw_score(self):
        # middle line
        pygame.draw.line(win, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
        # create txt
        score1 = H1.render(str(ball.score1_ball), True, WHITE)
        score2 = H1.render(str(ball.score2_ball), True, WHITE)

        # get rect of each text to center them
        score1_rect = score1.get_rect()
        score1_rect.center = WIDTH / 2 - 20, 20

        score2_rect = score2.get_rect()
        score2_rect.center = WIDTH / 2 + 20, 20

        win.blit(score1, score1_rect)
        win.blit(score2, score2_rect)


game = Main_game()
while game.running:
    game.controller()
    pygame.display.flip()
    clock.tick(FPS)
