import pygame
import random
import os

PINK = (255, 0, 160)
RED = (255, 0, 0)
PEACH = (255, 118, 95)
BLUE = (0, 0, 255)
BLUE_1 = (38, 0, 160)
DARK_YELLOW = (255, 174, 0)
GREEN = (38, 137, 0)
ORANGE = (255, 81, 0)
WHITE = (255, 255, 255)

COLORS = [PINK, RED, PEACH, BLUE, BLUE_1, DARK_YELLOW, GREEN, ORANGE, WHITE]
PLANE_IMAGE = r'{}\planne.png'.format(os.getcwd())
IMG = pygame.image.load(PLANE_IMAGE)
HORIZONTAL_VELOCITY = 0
VERTICAL_VELOCITY = 0

#change image size
image = pygame.transform.scale(IMG, (25, 25))

class Plane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Plane, self).__init__()
        self.image = image.convert()
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(random.choice(COLORS))
        self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.rect.x = x
        self.rect.y = y
        self.__vx = HORIZONTAL_VELOCITY
        self.__vy = VERTICAL_VELOCITY

    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy

    def get_plane_number(self):
        return self.plane_number
