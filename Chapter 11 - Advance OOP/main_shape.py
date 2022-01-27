import pygame
import random

from shapes import Ball

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

IMAGE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\galaxy image.jfif"

NUMBER_OF_BALLS = 5
DISTANCE = 50

REFRESH_RATE = 25
MAX_VELOCITY = 30

LEFT = 1
SCROLL = 2
RIGHT = 3

def is_on_edge(x, y):
    """ The function gets two integers,
        which represent the position of an image on screen
        the function will check if the position is over the screen size
        Args: x, y - integers
        Returns: True / False"""

    if x < 0 and x > 0:
        return False
    elif y < 0 and y > 0:
        return False


def main():

    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    image_background = pygame.image.load(IMAGE)
    screen.blit(image_background, (0, 0))

    balls_list = pygame.sprite.Group()
    for i in range(NUMBER_OF_BALLS):
        ball = Ball(i * DISTANCE, i * DISTANCE)
        balls_list.add(ball)
    balls_list.draw(screen)

    pygame.display.flip()

    finish = True
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            # add a ball each time user clicks mouse
            elif event.type == pygame.MOUSEBUTTONDOWN \
                 and event.button == LEFT:
                x, y = pygame.mouse.get_pos()
                ball = Ball(x, y)
                vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
                vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
                ball.update_v(vx, vy)
                balls_list.add(ball)
            for ball in balls_list:
                ball.update_loc()

        # update screen with balls
        screen.blit(image_background, (0, 0))
        balls_list.draw(screen)
        pygame.display.flip()
        clock.tick(REFRESH_RATE)


if __name__ == "__main__":
    main()
