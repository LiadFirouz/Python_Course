import pygame
import tkinter
from tkinter import filedialog as fd

# Setting permanent variable
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED1 = (255, 0, 255)
WHITE = (255, 255, 255)

PLAYER_IMAGE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\star.jpg"
SOUND_FILE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\Laser Sound Effect.wav"

REFRESH_RATE = 25

LEFT = 1
SCROLL = 2
RIGHT = 3

IMAGE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 11 - Advance OOP\galaxy image.jfif"


def choose_image_background():
    """ import image background from the user"""
    select_image_window = tkinter.Tk()
    select_image_window.title('Choose image for background')
    select_image_window.resizable(False, False)
    select_image_window.geometry('300x300')
    select_image_window.winfo_visualsavailable(False)
    user_image = fd.askopenfile(parent=select_image_window, initialdir="/", \
                                title='Please select your photo', filetypes=[
            ("image", ".jpeg"),
            ("image", ".png"),
            ("image", ".jpg"),
            ("image", ".jfif"),
        ])

    select_image_window.destroy()

    return user_image.name


def game_setup():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND_FILE)
    pygame.mouse.set_visible(False)

    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    # image = r'{}'.format(choose_image_background())
    # image_background = pygame.image.load(image)
    image_background = pygame.image.load(IMAGE)
    player_image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)
    screen.blit(image_background, (0, 0))
    pygame.display.flip()


def main():
    game_setup()
    clock = pygame.time.Clock()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    player_image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
    image_background = pygame.image.load(IMAGE)

    finish = True
    mouse_pos_list = []
    while finish:
        for event in pygame.event.get():
            mouse_point = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                finish = False
            elif event.type == pygame.MOUSEBUTTONDOWN \
                    and event.button == LEFT:
                mouse_pos_list.append(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN \
                    and event.button == RIGHT:
                pygame.mixer.music.play()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mouse_point = [mouse_point[0] - 10, mouse_point[1]]
                elif event.key == pygame.K_RIGHT:
                    mouse_point = [mouse_point[0] + 10, mouse_point[1]]
                elif event.key == pygame.K_UP:
                    mouse_point = [mouse_point[0], mouse_point[1] - 10]
                elif event.key == pygame.K_DOWN:
                    mouse_point = [mouse_point[0], mouse_point[1] + 10]

                elif event.key == pygame.K_SPACE:
                    mouse_pos_list.clear()

                pygame.mouse.set_pos(mouse_point)

        screen.blit(image_background, (0, 0))
        screen.blit(player_image, mouse_point)
        for clicked in mouse_pos_list:
            screen.blit(player_image, clicked)
        pygame.display.flip()


if __name__ == "__main__":
    main()
