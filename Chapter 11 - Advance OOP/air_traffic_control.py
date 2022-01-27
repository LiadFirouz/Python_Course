""" Pygame game example program
    Air traffic control
    Author: Liad Firouz """

import pygame
import random
from shapes import Plane

REFRESH_RATE = 25
MAX_VELOCITY = 30
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
NUMBER_OF_LINES = 10
BACKGROUND_IMAGE = r'C:\Users\liadf\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\sky.jpg'

LEFT_CLICK = 1
BLACK = (0, 0, 0)

PLANE_SIZE = 30
NUMBER_OF_PLANES = 4

# game first setup
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load(BACKGROUND_IMAGE)
pygame.display.set_caption("Air Traffic Control - score: {}".format(0))
screen.blit(background_image, (0, 0))
clock = pygame.time.Clock()


def set_matrix_on_screen(screen):
    """ Set matrix on the background
        Args: screen - pygame.surface """

    x_line_distance = WINDOW_WIDTH / NUMBER_OF_LINES
    y_line_distance = WINDOW_HEIGHT / NUMBER_OF_LINES

    # lines setup start and end set_cellss
    start_pos_width = [0, 0]
    end_pos_width = [0, WINDOW_HEIGHT]
    start_pos_height = [0, 0]
    end_pos_height = [WINDOW_WIDTH, 0]

    for i in range(NUMBER_OF_LINES):
        start_pos_width[0] += x_line_distance
        end_pos_width[0] += x_line_distance
        pygame.draw.line(screen, BLACK, start_pos_width, end_pos_width, width=1)
        start_pos_height[1] += y_line_distance
        end_pos_height[1] += y_line_distance
        pygame.draw.line(screen, BLACK, start_pos_height, end_pos_height, width=1)


def set_cells(x_distance, y_distance):
    """ Divided the screen into cells according to the
        matrix on the background
        Args: x_distance, y_distance - integers
        Returns: list - a list with all the cells"""

    cell_x_pos = 0
    cell_y_pos = 0
    cells_list = []

    for y in range(NUMBER_OF_LINES - 1):
        for x in range(NUMBER_OF_LINES - 1):
            x_center = (cell_x_pos + cell_x_pos + x_distance) / 2
            y_center = (cell_y_pos + cell_y_pos + y_distance) / 2
            cells_list.append([x_center, y_center])
            cell_x_pos += x_distance
        cell_y_pos += x_distance
        cell_x_pos = 0
    return cells_list


cells_list = set_cells(WINDOW_WIDTH / NUMBER_OF_LINES, WINDOW_HEIGHT / NUMBER_OF_LINES)
planes_list = pygame.sprite.Group()
new_planes_list = pygame.sprite.Group()


def is_cell_taken(cell):
    """ Checks if the cell that was drawn is already taken,
        if its taken drawn a new cell, else return the cell
        Args: cell - list [integer, integer]
        Returns: cell - list [integer, integer] """

    for plane in planes_list:
        x, y = plane.get_pos()
        if x == cell[0] - PLANE_SIZE and y == cell[1] - PLANE_SIZE:
            return is_cell_taken(random.choice(cells_list))
    return cell


def set_planes_positions(plane, cell):
    """ the function will receive a plane and create a new location for it
        Args: plane - Plane.shapes
              cell - list[integer, integer]"""
    plane.update_v(cell[0] - PLANE_SIZE, cell[1] - PLANE_SIZE)
    print(cell[0] - PLANE_SIZE, cell[1] - PLANE_SIZE)
    plane.update_loc()
    planes_list.add(plane)


# create planes
for i in range(NUMBER_OF_PLANES):
    plane = Plane(0, 0)
    cell = is_cell_taken(random.choice(cells_list))
    set_planes_positions(plane, cell)
planes_list.draw(screen)


def there_is_any_collisions():
    """ Check if there is any collisions between the planes
        Returns: True / False """

    new_planes_list.empty()
    for plane in planes_list:
        planes_hit_list = pygame.sprite.spritecollide \
            (plane, planes_list, False)
        if not len(planes_hit_list) == 1:
            return False
    return True


def possible_pos(plane):
    """ making a new list with all the options to move
        Args: plane - Plane.shapes
        Return: possible_pos - list[integer, integer]"""

    x_line_distance = WINDOW_WIDTH / NUMBER_OF_LINES
    y_line_distance = WINDOW_HEIGHT / NUMBER_OF_LINES
    x, y = plane.get_pos()
    x = x + PLANE_SIZE
    y = y + PLANE_SIZE

    possible_pos = []

    for cell in cells_list:
        if (cell[0] == x + x_line_distance or cell[0] == x - x_line_distance) \
                and cell[1] == y:
            possible_pos.append(cell)
        elif (cell[0] == x + x_line_distance or cell[0] == x - x_line_distance) \
                and cell[1] == y - y_line_distance:
            possible_pos.append(cell)
        elif (cell[0] == x + x_line_distance or cell[0] == x - x_line_distance) \
                and cell[1] == y + y_line_distance:
            possible_pos.append(cell)

    return possible_pos


def update_plane_number(plane_number):
    """ Updates the plane
        Args: plane_number - integer
        Returns: plane_number - integer"""
    if plane_number + 1 < NUMBER_OF_PLANES:
        plane_number += 1
    else:
        plane_number = 0
    return plane_number


def choose_plane(plane_number, plane_list):
    for plane in enumerate(plane_list):
        if plane[0] == plane_number:
            return plane[1]


def main():
    score = 0
    plane_number = 0

    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                x, y = pygame.mouse.get_pos()
                print(x, y)

        while True: # there_is_any_collisions():

            plane = choose_plane(plane_number, planes_list)
            print('lll' ,len(possible_pos(plane)))
            cell = (random.choice(possible_pos(plane)))
            set_planes_positions(plane, cell)
            update_plane_number(plane_number)
            print('good')
            # update screen
            screen.blit(background_image, (0, 0))
            set_matrix_on_screen(screen)
            planes_list.draw(screen)
            pygame.display.flip()
            clock.tick(REFRESH_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()
