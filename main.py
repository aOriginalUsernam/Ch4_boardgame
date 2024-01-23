import pygame
import pyautogui
import os
from grid import *
from block import Block
from shape import Shape
from shapes import Shapes


def __main__() -> None:
    margin = 230
    width_and_height = 10  # int(input("Board size: "))
    cell_size = 50
    width = width_and_height * cell_size + 2 * margin
    height = width_and_height * cell_size + 2 * margin

    pygame.init()

    # make full screen
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

    # load block image
    r_block_img = pygame.image.load(os.path.join(os.getcwd(), "images\\block_red.png"))

    # make block
    my_block = Block(200, 200, cell_size - 0.5, r_block_img)
    test = Shape(my_block, Shapes.Z_BLOCK)

    # main game loop
    game_over = False
    is_dragging_shape = False
    while True:
        try:
            if game_over:
                raise SystemExit

            # player input
            if is_dragging_shape:
                x, y = pygame.mouse.get_pos()
                test.move(x, y)
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        raise SystemExit
                    case pygame.MOUSEBUTTONUP:
                        is_dragging_shape = False
                        for item in test.sprites():
                            if item.rect.collidepoint(x, y):
                                closest_grid_x_and_y = closest_grid(cell_centers, x, y)
                                x, y = closest_grid_x_and_y
                                test.move(x, y)
                    case pygame.MOUSEBUTTONDOWN:
                        # what to do when mouse down
                        x, y = pygame.mouse.get_pos()
                        for item in test.sprites():
                            if item.rect.collidepoint(x, y):
                                is_dragging_shape = True
                                break
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                raise SystemExit

            # update screen
            draw_grid(screen, cell_size, width_and_height, margin)
            test.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        except SystemExit:
            pygame.quit()
            break


if __name__ == "__main__":
    __main__()
