import pygame
import os

PINK = (255, 20, 147)
WHITE = (255, 255, 255)

PLANE_IMAGE = r'{}\planne.png'.format(os.getcwd())
HORIZONTAL_VELOCITY = 0
VERTICAL_VELOCITY = 0


class Plane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Plane, self).__init__()
        self.image = pygame.image.load(PLANE_IMAGE).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
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

