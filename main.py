import pygame
import pyautogui
import os
from grid import draw_grid
from block import Block
from shape import Shape
from shapes import Shapes


def __main__() -> None:
    width, height = 700, 600
    grid_size = 7
    cell_size = width // grid_size

    pygame.init()

    # make full screen
    full_screen_size = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    draw_grid(screen, cell_size, grid_size)

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
    my_block = Block(200, 200, cell_size, r_block_img)
    test = Shape(my_block, Shapes.TWOBYTWO)

    # main game loop
    game_over = False
    while True:
        try:
            if game_over:
                raise SystemExit

            # player input
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        raise SystemExit
                    case pygame.MOUSEBUTTONUP:
                        # what to do when mouse up
                        pass
                    case pygame.MOUSEBUTTONDOWN:
                        # what to do when mouse down
                        pass
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                raise SystemExit

            # update screen
            test.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        except SystemExit:
            pygame.quit()
            break


if __name__ == "__main__":
    __main__()
