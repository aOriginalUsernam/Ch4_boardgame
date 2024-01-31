import pygame
import pyautogui
import os
from grid import *
from block import Block
from game_loop import GameLoop
from shape import Shape
from shapes import Shapes
from shapeHandler import ShapeHandler
from text import Timer, Button, Points, Image
from board import Board
import random
from menu import *


def __main__() -> None:
    pygame.init()
    try:
        full_screen_size = pyautogui.size()
        screen = pygame.display.set_mode((full_screen_size[0], full_screen_size[1]))
        clock = pygame.time.Clock()
        cell_amount = get_board_size(clock, screen)
        margin = 230
        cell_size = 50
        margin = cell_size * 4 + 20
        width = cell_amount * cell_size + 2 * margin
        height = cell_amount * cell_size + 2 * margin
        screen = pygame.display.set_mode((width, height))

        # make header
        pygame.display.set_caption("boardgame")
        icon = pygame.image.load(os.path.join(os.getcwd(), "images/siep.jpg")).convert()
        pygame.display.set_icon(icon)

        # run start
        resp = start_screen(clock, screen)
        if resp == 0:
            raise SystemExit
        elif resp == 1:
            loop = GameLoop(
                clock, screen, (width, height), margin, cell_amount, cell_size
            )
        elif resp == 2:
            loop = GameLoop(
                clock, screen, (width, height), margin, cell_amount, cell_size, True
            )
        # run game
        resp = loop.play_game(screen)
        pass
    except SystemExit:
        pygame.quit()


if __name__ == "__main__":
    __main__()
