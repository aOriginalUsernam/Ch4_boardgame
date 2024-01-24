import pygame
import pyautogui
import os
from grid import *
from block import Block

from shape import Shape
from shapes import Shapes
from shapeHandler import ShapeHandler
from text import Timer
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

    # make timer
    texts = pygame.sprite.Group()
    font = pygame.font.Font(None, 36)
    timer = Timer(font, int(width / 2), 36 / 2, 10)
    texts.add(timer)

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
                timer.reset()
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
                        is_valid = True
                        item = shape.sprites()[0]
                        # if inside of a board it has no valid pos
                        for board in [p1_board, p2_board]:
                            if board.left <= x and board.right >= x:
                                is_valid = False
                                break

                        # get closest grid and check if shape has valid pos
                        if (
                            item.rect.collidepoint(x, y)
                            or shape.shape == Shapes.S_BLOCK
                        ) and is_valid:
                            closest_grid_x_and_y, closest_index = closest_grid(
                                cell_centers, x, y
                            )
                            x, y = closest_grid_x_and_y
                            is_valid = shape_handler.check_is_valid_pos(
                                x,
                                y,
                                shape.shape,
                                width_and_height,
                                cell_size,
                                closest_index,
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
            texts.draw(screen)

            pygame.display.flip()
            try:
                timer.tick()
            except:
                game_over = True
            clock.tick(60)

        except SystemExit:
            pygame.quit()
            break


if __name__ == "__main__":
    __main__()
