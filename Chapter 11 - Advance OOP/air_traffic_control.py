""" Pygame game example program
    Air traffic control
    Author: Liad Firouz """

import pygame
import random
import os
import sys
from tkinter import *
from tkinter import messagebox
from shapes import Plane

# window set-up
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
NUMBER_OF_LINES = 10
BACKGROUND_IMAGE = r'{}\sky.jpg'.format(os.getcwd())

PLANE_SIZE = 30
NUMBER_OF_PLANES = 10
VX_DISTANCE = WINDOW_WIDTH / NUMBER_OF_LINES
VY_DISTANCE = WINDOW_HEIGHT / NUMBER_OF_LINES

REFRESH_RATE = 25
MAX_VELOCITY = 30

LEFT_CLICK = 1
BLACK = (0, 0, 0)


def set_matrix_on_screen(screen):
    """ Set matrix on the background
        Args: screen - pygame.surface """

    x_line_distance = WINDOW_WIDTH / NUMBER_OF_LINES
    y_line_distance = WINDOW_HEIGHT / NUMBER_OF_LINES

    # lines setup start and end set_cells
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


def is_cell_taken(cell):
    """ Checks if the cell that was drawn is already taken,
        if its taken drawn a new cell, else return the cell
        Args: cell - list [integer, integer]
        Returns: cell - list [integer, integer] """

    for plane in planes_list:
        x, y = plane.get_pos()
        if x == cell[0] and y == cell[1]:
            return is_cell_taken(random.choice(cells_list))
    return cell


def set_planes_positions(plane, cell):
    """ the function will receive a plane and create a new location for it
        Args: plane - Plane.shapes
        cell - list[integer, integer]"""
    plane.update_v(cell[0], cell[1])
    plane.update_loc()
    planes_list.add(plane)


def choose_plane(plane_number, plane_list):
    for plane in enumerate(plane_list):
        if plane[0] == plane_number:
            return plane[1]


def plane_next_optinal_cells(plane, planes_positions):
    """ making a new list with all the options to move
        Args: plane - Plane.shapes
        Return: possible_pos - list[integer, integer]"""

    current_x, current_y = plane.get_pos()
    optinal_cells = []

    for cell in cells_list:
        if (cell[0] == current_x + VX_DISTANCE or cell[0] == current_x - VX_DISTANCE) \
                and cell[1] == current_y:
            optinal_cells.append(cell)
        elif (cell[0] == current_x + VX_DISTANCE or cell[0] == current_x - VX_DISTANCE \
              or cell[0] == current_x) and cell[1] == current_y - VY_DISTANCE:
            optinal_cells.append(cell)
        elif (cell[0] == current_x + VX_DISTANCE or cell[0] == current_x - VX_DISTANCE \
              or cell[0] == current_x) and cell[1] == current_y + VY_DISTANCE:
            optinal_cells.append(cell)

    for position in planes_positions:
        for cell in optinal_cells:
            x = cell[0]
            y = cell[1]
            px = position[0]
            py = position[1]
            if x == px and y == py:
                optinal_cells.remove(cell)

    return optinal_cells


def update_plane_number(plane_number):
    """ Updates the plane
        Args: plane_number - integer
        Returns: plane_number - integer"""
    if plane_number + 1 < NUMBER_OF_PLANES:
        plane_number += 1
    else:
        plane_number = 0
    return plane_number


def collisions(planes_positions):

    for p in planes_positions:
        more_then_one = 0
        for p1 in planes_positions:
            if p == p1:
                more_then_one += 1
            if more_then_one > 1:
                return True
    return False

# game initialize
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load(BACKGROUND_IMAGE)
pygame.display.set_caption("Air Traffic Control - score: {}".format(0))
screen.blit(background_image, (0, 0))
clock = pygame.time.Clock()

# create board
cells_list = set_cells(WINDOW_WIDTH / NUMBER_OF_LINES, WINDOW_HEIGHT / NUMBER_OF_LINES)
planes_list = pygame.sprite.Group()
planes_positions = []

# create planes
for i in range(NUMBER_OF_PLANES):
    plane = Plane(0, 0)
    cell = is_cell_taken(random.choice(cells_list))
    set_planes_positions(plane, cell)
    planes_positions.append(plane.get_pos())
planes_list.draw(screen)


def main():
    score = 0
    ticks = 0
    plane_number = 0

    while ticks < 4000 and not collisions(planes_positions):  # collisions():

        # reaction for the x button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for plane in planes_list:
            try:
                next_cell = random.choice(plane_next_optinal_cells(plane, planes_positions))
                score += 200
            except Exception as e:  # if their error which error print...
                print("Error: {}".format(e))

            current_x, current_y = plane.get_pos()
            set_planes_positions(plane, [next_cell[0] - current_x, next_cell[1] - current_y])
            planes_positions[plane_number] = plane.get_pos()
            print([next_cell[0] - current_x, next_cell[1] - current_y], '\n')
            plane_number = update_plane_number(plane_number)
            ticks += 1

        # update changes on screen
        screen.blit(background_image, (0, 0))
        pygame.display.set_caption("Air Traffic Control - tour: {}".format(ticks))
        set_matrix_on_screen(screen)
        planes_list.draw(screen)
        clock.tick(REFRESH_RATE * 100)
        pygame.display.flip()
        clock.tick(REFRESH_RATE * 0.1)

    Tk().wm_withdraw()  # to hide the main window
    if not(score < 3800 and not collisions(planes_positions)):
        messagebox.showinfo('You Won', 'Yes!')
    else:
        messagebox.showinfo('Game End', 'OK')
    pygame.quit()


if __name__ == "__main__":
    main()

