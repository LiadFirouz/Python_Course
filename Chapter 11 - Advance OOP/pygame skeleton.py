import pygame
import math

# Setting screen size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Setting colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Setting image background
IMAGE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\galaxy image.jfif"

# Setting time for the timer
REFRESH_RATE = 25

# Setting radios
RADIUS = 30

# Starting to initialize pygame
pygame.init()

# Create the screen display
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)

# Setting the screen background color
# screen.fill(WHITE)

# Setting and displaying the screen background image
img = pygame.image.load(IMAGE)
screen.blit(img, (0, 0))
pygame.display.flip()

# Display a line on the screen
# pygame.draw.line(surface, color, start_pos, end_pos, width=1)
"""
line_length = 300
for i in range(101):
    angle = i * 3.6
    x = screen.get_rect().centerx + math.sin(angle) * line_length
    y = screen.get_rect().centery + math.cos(angle) * line_length
    pygame.draw.line(screen, RED, screen.get_rect().center, [x, y], width=1)
pygame.draw.circle(screen, RED, [screen.get_rect().centerx, screen.get_rect().centery], 30, 30)
pygame.display.flip()
"""

clock = pygame.time.Clock()
ball_x_pos = 0
ball_y_pos = 0

finish = False
while not finish:

    # 'Game' is the screen name
    pygame.display.set_caption("Game")
    for event in pygame.event.get():

        # If the user press on X to close the windows (pygame.event.get())
        if event.type == pygame.QUIT:
            finish = True

    screen.blit(img, (0, 0))
    ball_x_pos += 10
    ball_y_pos += 10

    pygame.draw.circle(screen, WHITE, [ball_x_pos, ball_y_pos], RADIUS)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)
