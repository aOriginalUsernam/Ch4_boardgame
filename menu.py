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
    font = pygame.font.SysFont("Georgia", 80, bold=True)

    # start button
    start_btn = Button(font, "START", screen.get_width() / 100 * 35, screen.get_height() / 100 * 25)

    load_btn = Button(font, "LOAD GAME", screen.get_width() / 100 * 22, screen.get_height() / 100 * 45)

    # quit button
    quit_btn = Button(font, "QUIT", screen.get_width() / 100 * 38, screen.get_height() / 100 * 65)

    btns = pygame.sprite.Group()
    btns.add(start_btn, load_btn, quit_btn)
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
                        elif load_btn.rect.collidepoint(event.pos):
                            return 2
        # draw start buttons
        btns.draw(screen)

        pygame.display.flip()
        clock.tick(15)


def pause_screen(clock: pygame.time.Clock, screen: pygame.surface.Surface) -> int:
    # make buttons
    font = pygame.font.SysFont("Georgia", 80, bold=True)

    # start button
    resume_btn = Button(font, "RESUME", screen.get_width() / 100 * 30, screen.get_height() / 100 * 25)

    save_btn = Button(font, "SAVE", screen.get_width() / 100 * 38, screen.get_height()/ 100 * 45)

    # quit button
    quit_btn = Button(font, "QUIT", screen.get_width() / 100 * 38, screen.get_height() / 100 * 65)

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


def get_names(clock: pygame.time.Clock, screen: pygame.surface.Surface, initial_text="", max_length=14) -> int:
    font = pygame.font.SysFont("Georgia", 40, bold=True)
    input_text = initial_text
    input_rect = pygame.Rect(screen.get_width() / 100 * 32, screen.get_height() / 100 * 45, 350, 50)
    active = True
    
    while active:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < max_length:
                        input_text += event.unicode
                        
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
        rendered_text = font.render(input_text, True, (255, 255, 255))
        screen.blit(rendered_text, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()
        clock.tick(15)
    
    return input_text