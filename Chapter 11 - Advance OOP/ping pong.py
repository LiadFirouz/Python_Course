import pygame
import math

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
PLAYER_IMAGE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\star.jpg"
# Setting time for the timer
REFRESH_RATE = 25
# Setting radios
RADIUS = 30
# Setting mouse clickers
LEFT = 1
SCROLL = 2
RIGHT = 3

# Starting to initialize pygame
pygame.init()

# Setting mouse invisible
pygame.mouse.set_visible(False)

# Create the screen display
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)

# Setting the screen background color
# screen.fill(WHITE)

# Setting and displaying the screen background image
img = pygame.image.load(IMAGE)
player_image = pygame.image.load(PLAYER_IMAGE)
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

# pygame animation
"""
clock = pygame.time.Clock()
ball_x_pos = WINDOW_WIDTH / 2
ball_y_pos = WINDOW_HEIGHT / 2

finish = False
movement = 10
while not finish:

    # 'Game' is the screen name
    pygame.display.set_caption("Ping Pong")
    for event in pygame.event.get():

        # If the user press on X to close the windows (pygame.event.get())
        if event.type == pygame.QUIT:
            finish = True

    screen.blit(img, (0, 0))

    # 0<y<300 and 0<x<300
    if 0 <= ball_y_pos < WINDOW_HEIGHT / 2 and 0 < ball_x_pos < WINDOW_WIDTH / 2:
        ball_x_pos -= 10
        ball_y_pos += 10
        c = WHITE

    # 300<y<600 and 300<x<600
    elif WINDOW_HEIGHT / 2 <= ball_y_pos <= WINDOW_HEIGHT and WINDOW_WIDTH / 2 <= ball_x_pos <= WINDOW_WIDTH:
        ball_x_pos += 10
        ball_y_pos -= 10
        c = RED

    # 0<y<300 and 300<x<600
    elif 0 < ball_y_pos < WINDOW_HEIGHT / 2 and WINDOW_WIDTH / 2 <= ball_x_pos <= WINDOW_WIDTH:
        ball_x_pos -= 10
        ball_y_pos -= 10
        c = BLACK

    # 300<y<600 and 0<x<300
    elif WINDOW_HEIGHT / 2 <= ball_y_pos < WINDOW_HEIGHT and 0 < ball_x_pos < WINDOW_WIDTH / 2:
        ball_x_pos += 10
        ball_y_pos += 10
        c = RED1

    print(ball_x_pos, ball_y_pos)

    pygame.draw.circle(screen, c, [ball_x_pos, ball_y_pos], RADIUS)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)"""

# pygame mouse event
finish = False
clock = pygame.time.Clock()

mouse_pos_list = []
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_pos_list.append(pygame.mouse.get_pos())
    screen.blit(img, (0, 0))
    mouse_point = pygame.mouse.get_pos()
    print(mouse_point)
    screen.blit(player_image, mouse_point)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)
