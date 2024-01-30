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
                            return 1
                        elif quit_btn.rect.collidepoint(event.pos):
                            pygame.quit()
                            return 0
        # draw start buttons
        btns.draw(screen)

        pygame.display.flip()
        clock.tick(15)


def pause_screen(clock: pygame.time.Clock, screen: pygame.surface.Surface) -> int:
    # make buttons
    font = pygame.font.SysFont("Georgia", 40, bold=True)

    # start button
    resume_btn = Button(font, "RESUME", screen.get_width() / 4, screen.get_height() / 2)

    save_btn = Button(font, "SAVE", screen.get_width() / 4 * 1.5, screen.get_height()/ 2)

    # quit button
    quit_btn = Button(font, "QUIT", screen.get_width() / 4 * 3, screen.get_height() / 2)

    btns = pygame.sprite.Group()
    btns.add(resume_btn, save_btn, quit_btn)
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return 0
                case pygame.MOUSEBUTTONUP:
                    if resume_btn in btns:
                        if resume_btn.rect.collidepoint(event.pos):
                            button_press_sound.play()
                            pygame.mixer.music.play(-1)
                            return 1
                        elif save_btn.rect.collidepoint(event.pos):
                            button_press_sound.play()
                            return 2
                        elif quit_btn.rect.collidepoint(event.pos):
                            pygame.quit()
                            return 0
        # draw start buttons
        btns.draw(screen)

        pygame.display.flip()
        clock.tick(15)
