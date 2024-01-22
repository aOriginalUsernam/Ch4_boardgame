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
                    case pygame.KEYDOWN:
                        # what to do when a key down
                        pass
                    case pygame.KEYUP:
                        # what to do when a key up
                        pass

            # update screen
            pygame.display.flip()
            clock.tick(60)
        except SystemExit:
            pygame.quit()
            break
