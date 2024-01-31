import pygame
import os
from text import Button, Text
import time


def start_screen(clock: pygame.time.Clock, screen: pygame.surface.Surface) -> int:
    # press sound
    button_press_sound = pygame.mixer.Sound(
        os.path.join(os.getcwd(), "sounds\\button_press.mp3")
    )

    # make buttons
    font = pygame.font.SysFont("Georgia", 80, bold=True)

    # start button
    start_btn = Button(
        font, "START", screen.get_width() / 2, screen.get_height() / 100 * 25
    )

    load_btn = Button(
        font, "LOAD GAME", screen.get_width() / 2, screen.get_height() / 100 * 45
    )

    # quit button
    quit_btn = Button(
        font, "QUIT", screen.get_width() / 2, screen.get_height() / 100 * 65
    )

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
    # button sound
    button_press_sound = pygame.mixer.Sound(
        os.path.join(os.getcwd(), "sounds\\button_press.mp3")
    )
    # make buttons
    font = pygame.font.SysFont("Georgia", 80, bold=True)

    # start button
    resume_btn = Button(
        font, "RESUME", screen.get_width() / 2, screen.get_height() / 100 * 25
    )

    save_btn = Button(
        font, "SAVE", screen.get_width() / 2, screen.get_height() / 100 * 45
    )

    # quit button
    quit_btn = Button(
        font, "QUIT", screen.get_width() / 2, screen.get_height() / 100 * 65
    )

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


def win_screen(
    clock: pygame.time.Clock,
    screen: pygame.surface.Surface,
    cell_amount: tuple,
    points=None,
    winner=None,
) -> int:
    yay_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "sounds\\yay.mp3"))
    trombone_sound = pygame.mixer.Sound(
        os.path.join(os.getcwd(), "sounds\\trombone.mp3")
    )

    if cell_amount <= 9:
        size = cell_amount * 8
    else:
        size = cell_amount * 6

    font = pygame.font.SysFont("Georgia", size, bold=True)

    # checks if its a draw or not
    if winner != None:
        yay_sound.play()
        winner_text = Text(font, f"Winner is {winner}", screen.get_width() / 2, 200)

        if points == 1:
            points_text = Text(
                font, f"with {points} point", screen.get_width() / 2, 300
            )
        else:
            points_text = Text(
                font, f"with {points} points", screen.get_width() / 2, 300
            )

        quit_btn = Button(
            font, "QUIT", screen.get_width() / 2, screen.get_height() / 100 * 65
        )

    else:
        trombone_sound.play()
        winner_text = Text(font, f"Game ended in a draw", screen.get_width() / 2, 200)
        quit_btn = Button(
            font, "QUIT", screen.get_width() / 2, screen.get_height() / 100 * 65
        )

    btns = pygame.sprite.Group()

    if points == None:
        btns.add(winner_text, quit_btn)
    else:
        btns.add(winner_text, points_text, quit_btn)

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return 0
                case pygame.MOUSEBUTTONUP:
                    if quit_btn in btns:
                        if quit_btn.rect.collidepoint(event.pos):
                            raise SystemExit
                            # pygame.quit()
                            # return 0
        # draw buttons n text
        btns.draw(screen)

        pygame.display.flip()
        clock.tick(15)


def get_names(
    clock: pygame.time.Clock,
    screen: pygame.surface.Surface,
    initial_text: str,
    max_length=14,
) -> tuple[str, str]:
    font = pygame.font.SysFont("Georgia", 40, bold=True)
    input_text = initial_text
    input_rect = pygame.Rect(
        screen.get_width() / 100 * 32, screen.get_height() / 100 * 45, 360, 50
    )
    active = True

    while active:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = ""
                else:
                    if len(input_text) < max_length:
                        input_text += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
        rendered_text = font.render(input_text, True, (255, 255, 255))
        screen.blit(rendered_text, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()
        clock.tick(15)

    return input_text


def get_board_size(
    clock: pygame.time.Clock,
    screen: pygame.surface.Surface,
    initial_digit="Board size; Number between 7-13",
    max_length=2,
):
    input_digit = initial_digit
    font = pygame.font.SysFont("Georgia", 40, bold=True)
    input_rect = pygame.Rect(
        screen.get_width() / 100 * 32, screen.get_height() / 100 * 45, 700, 50
    )
    active = True

    while active:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        board_size = int(input_digit)
                        if 7 <= board_size <= 13:
                            return board_size
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    input_digit = ""
                elif len(input_digit) < max_length:
                    input_digit += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
        rendered_text = font.render(input_digit, True, (255, 255, 255))
        screen.blit(rendered_text, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()
        clock.tick(15)

    return input_digit
