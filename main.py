import pygame
import pyautogui
import os
from grid import *
from block import Block

from shape import Shape
from shapes import Shapes
from shapeHandler import ShapeHandler
import random


def __main__() -> None:
    margin = 230
    width_and_height = 10  # int(input("Board size: "))
    cell_size = 50
    width = width_and_height * cell_size + 2 * margin
    height = width_and_height * cell_size + 2 * margin

    pygame.init()

    # make grid
    full_screen_size = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    cell_centers = draw_grid(screen, cell_size, width_and_height, margin)

    # make header
    pygame.display.set_caption("boardgame")
    icon = pygame.image.load(os.path.join(os.getcwd(), "images/siep.jpg")).convert()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    # make mouse
    curs = pygame.Cursor()
    pygame.mouse.set_cursor(curs)

    # MAKE PLAYER BOARD
    p1_board = pygame.Rect(0, 0, margin, height)
    p2_board = pygame.Rect(width - margin, 0, margin, height)
    col = pygame.Color(10, 10, 10)

    # load block image
    r_block_img = pygame.image.load(os.path.join(os.getcwd(), "images\\block_red.png"))
    g_block_img = pygame.image.load(
        os.path.join(os.getcwd(), "images\\block_green.png")
    )

    # make block + shape handler
    red_block = Block(200, 200, cell_size - 0.5, r_block_img)
    green_block = Block(width - 200, 200, cell_size - 0.5, g_block_img)
    shape_handler = ShapeHandler()
    shape = shape_handler.generate_shape(red_block)

    # main game loop
    game_over = False
    is_dragging_shape = False
    is_player_1 = True
    while True:
        try:
            if game_over:
                raise SystemExit

            # if shape is placed generate new shape
            if shape.is_placed:
                if is_player_1:
                    shape = shape_handler.generate_shape(green_block)
                    is_player_1 = False
                else:
                    shape = shape_handler.generate_shape(red_block)
                    is_player_1 = True

            # player input
            if is_dragging_shape:
                x, y = pygame.mouse.get_pos()
                shape.move(x, y)
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        raise SystemExit
                    case pygame.MOUSEBUTTONUP:
                        is_dragging_shape = False
                        for item in shape.sprites():
                            if (
                                item.rect.collidepoint(x, y)
                                or shape.shape == Shapes.S_BLOCK
                            ):
                                closest_grid_x_and_y, closest_index = closest_grid(
                                    cell_centers, x, y
                                )
                                print(closest_index)
                                x, y = closest_grid_x_and_y
                                is_valid = shape.check_is_valid_pos(
                                    x, y, shape.shape, width_and_height, cell_size
                                )
                                if is_valid:
                                    shape.move(x, y)
                                    shape.is_placed = True
                    case pygame.MOUSEBUTTONDOWN:
                        # what to do when mouse down
                        x, y = pygame.mouse.get_pos()
                        for item in shape.sprites():
                            if item.rect.collidepoint(x, y):
                                is_dragging_shape = True
                                break
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                raise SystemExit

            # update screen
            draw_grid(screen, cell_size, width_and_height, margin)
            pygame.draw.rect(screen, col, p1_board)
            pygame.draw.rect(screen, col, p2_board)
            shape_handler.draw_shapes(screen)

            pygame.display.flip()
            clock.tick(60)

        except SystemExit:
            pygame.quit()
            break


if __name__ == "__main__":
    __main__()
