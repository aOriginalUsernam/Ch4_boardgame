import pygame
import os
from text import Button
import time

pygame.init()
# pygame.mixer.music.load(os.path.join(os.getcwd(), "data/sounds/m3.wav"))
# pygame.mixer.music.play(-1)
button_press_sound = pygame.mixer.Sound(
    os.path.join(os.getcwd(), "sounds\\button_press.mp3")
    )

pygame.mixer.music.load(os.path.join(os.getcwd(), "sounds\\Tetris.mp3"))
pygame.mixer.music.set_volume(0.05)


def start_screen(clock: pygame.time.Clock, screen: pygame.surface.Surface) -> int:
    # make buttons
    font = pygame.font.SysFont("Georgia", 40, bold=True)

    # start button
    start_btn = Button(font, "START", screen.get_width() / 4, screen.get_height() / 2)

    # quit button
    quit_btn = Button(font, "QUIT", screen.get_width() / 4 * 3, screen.get_height() / 2)

    btns = pygame.sprite.Group()
    btns.add(start_btn, quit_btn)
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return 0
                case pygame.MOUSEBUTTONUP:
                    if start_btn in btns:
                        if start_btn.rect.collidepoint(event.pos):
                            button_press_sound.play()
                            pygame.mixer.music.play(-1)
                            return 0
                        elif quit_btn.rect.collidepoint(event.pos):
                            pygame.quit()
                            return 0
        # draw start buttons
        btns.draw(screen)

        pygame.display.flip()
        clock.tick(15)