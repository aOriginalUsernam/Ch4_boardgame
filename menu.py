import pygame
import os

# pygame.init()
# # pygame.mixer.music.load(os.path.join(os.getcwd(), "data/sounds/m3.wav"))
# # pygame.mixer.music.play(-1)
# button_press = pygame.mixer.Sound(
#     os.path.join(os.getcwd(), "sounds\\button_press.mp3")
#     )

# button_press.play()
# pygame.time.delay(1000)



def start_screen(clock, screen):
    # Make buttons
    font = pygame.font.SysFont("Georgia", 40, bold=True)

    # Start button
    start_btn = Button(font, "START", screen.get_width() / 4, screen.get_height() / 2)

    # Quit button
    quit_btn = Button(font, "QUIT", screen.get_width() / 4 * 3, screen.get_height() / 2)

    # P1
    p1_btn = Button(font, "ONE PLAYER", screen.get_width() / 4, screen.get_height() / 2)

    # P2
    p2_btn = Button(font, "TWO PLAYERS", screen.get_width() / 4 * 3, screen.get_height() / 2)

    # Example usage to draw buttons
    buttons = [start_btn, quit_btn, p1_btn, p2_btn]
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

    # Example usage to check for button click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(pos):
                        if button.text == "START":
                            return 1  # Return an appropriate value for START button
                        elif button.text == "QUIT":
                            pygame.quit()
                            quit()
                        elif button.text == "ONE PLAYER":
                            return 2  # Return an appropriate value for ONE PLAYER button
                        elif button.text == "TWO PLAYERS":
                            return 3  # Return an appropriate value for TWO PLAYERS button