import pygame
import pyautogui
import os


def __main__() -> None:
    pygame.init()

    # make full screen
    full_screen_size = pyautogui.size()
    screen = pygame.display.set_mode(full_screen_size)

    # make header
    pygame.display.set_caption("boardgame")
    icon = pygame.image.load(os.path.join(os.getcwd(), "images/siep.jpg")).convert()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    # make mouse
    curs = pygame.Cursor()
    pygame.mouse.set_cursor(curs)

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
            pygame.display.flip()
            clock.tick(60)
        except SystemExit:
            pygame.quit()
            break


if __name__ == "__main__":
    __main__()
