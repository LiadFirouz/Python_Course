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
# Setting sound
SOUND_FILE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\Laser Sound Effect.wav"

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
player_image = pygame.image.load(PLAYER_IMAGE)
screen.blit(img, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()
finish = True
mouse_pos_list = []
while finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False
        elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == LEFT:
            pygame.mixer.music.play()
            mouse_pos_list.append(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pygame.mixer.music.play()

    screen.blit(img, (0, 0))
    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)
    for clicked in mouse_pos_list:
        screen.blit(player_image, clicked)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)
