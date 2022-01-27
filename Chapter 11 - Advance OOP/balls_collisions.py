""" Pygame exmaple program
    Move sprites randomly and detect collisions
    Author: Barak Gonen """

import pygame
import random
from shapes import Ball

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
LEFT = 1
BACKGROUND_IMAGE = r'C:\Users\liadf\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\galaxy image.jfif'
REFRESH_RATE = 25
BALL_SIZE = 30
MAX_VELOCITY = 30

img = pygame.image.load(BACKGROUND_IMAGE)
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
screen.blit(img, (0, 0))
clock = pygame.time.Clock()

balls_list = pygame.sprite.Group()
new_balls_list = pygame.sprite.Group()
finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        # add a ball each time user clicks mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            ball = Ball(x, y)
            vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
            vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
            ball.update_v(vx, vy)
            balls_list.add(ball)

        # update balls locations, bounce from edges
        for ball in balls_list:
            ball.update_loc()
            x, y = ball.get_pos()
            vx, vy = ball.get_v()
            if x + BALL_SIZE > WINDOW_WIDTH or x < 0:
                vx *= -1
            if y + BALL_SIZE > WINDOW_HEIGHT or y < 0:
                vy *= -1
            ball.update_v(vx, vy)

        # find which balls collide and should be removed
        new_balls_list.empty()
        for ball in balls_list:
            balls_hit_list = pygame.sprite.spritecollide \
                (ball, balls_list, False)
            if len(balls_hit_list) == 1:
                # ball collides
                # only with itself
                new_balls_list.add(ball)

        balls_list.empty()
        for ball in new_balls_list:
            balls_list.add(ball)

    # update screen with surviving balls
    screen.blit(img, (0, 0))
    balls_list.draw(screen)

    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()
