import pygame
import random
import math
from shapes import Ball

# Setting screen size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Setting colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED1 = (255, 0, 255)
# Setting image background
IMAGE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\galaxy image.jfif"
# Setting time for the timer
REFRESH_RATE = 25
# Setting radios
RADIUS = 30
# Setting mouse clickers
LEFT = 1
SCROLL = 2
RIGHT = 3
# Setting sound
SOUND_FILE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\Laser Sound Effect.wav"
MAX_VELOCITY = 30

# Starting to initialize pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
# Setting mouse invisible
pygame.mouse.set_visible(False)
# Create the screen display
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
# Setting and displaying the screen background image
img = pygame.image.load(IMAGE)
screen.blit(img, (0, 0))
pygame.display.flip()


def y_on_screen(y):
    """ The function gets two integers,
        which represent the position of an image on screen
        the function will check if the position is over the screen size
        Args: x, y - integers
        Returns: True / False"""

    if not 0 < y < WINDOW_HEIGHT:
        return False

    return True


def x_on_screen(x):
    """ The function gets two integers,
        which represent the position of an image on screen
        the function will check if the position is over the screen size
        Args: x, y - integers
        Returns: True / False"""

    if not 0 < x < WINDOW_WIDTH:
        return False

    return True


def main():
    clock = pygame.time.Clock()
    balls_list = pygame.sprite.Group()
    finish = True
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = False
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
            x, y = ball.get_pos()
            vx, vy = ball.get_v()
            if not x_on_screen(x):
                ball.update_v(vx * -1, vy)
                ball.update_loc()

            if not y_on_screen(y):
                ball.update_v(vx, vy * -1)
                ball.update_loc()

        new_balls_list = pygame.sprite.Group()
        balls_hit_list = 0
        new_balls_list.empty()
        for ball in balls_list:
            balls_hit_list = pygame.sprite.spritecollide(ball, balls_list, False)
        if len(balls_hit_list) == 1:
            # ball collides
            # only with itself
            new_balls_list.add(ball)
        balls_list.empty()

        for ball in new_balls_list:
            balls_list.add(ball)

        screen.blit(img, (0, 0))
        balls_list.draw(screen)
        pygame.display.flip()
        clock.tick(REFRESH_RATE)


if __name__ == "__main__":
    main()
