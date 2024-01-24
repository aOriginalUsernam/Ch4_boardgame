import pygame


class Timer(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, x: int, y: int, time: int = 30) -> None:
        super().__init__()
        self.font = font
        self.image = font.render(f"[{time}]", True, "white").convert_alpha()
        self.rect = pygame.Rect(
            x,
            y,
            self.image.get_width() + 10,
            self.image.get_height() + 10,
        )
        self.start_time = time
        self.time = time
        self.curent_tick = 0

    def tick(self):
        self.curent_tick += 1
        if self.curent_tick == 60:
            self.curent_tick = 0
            self.time -= 1
            if self.time < 0:
                raise SystemExit
            self.image = self.font.render(f"[{self.time}]", True, "white")

    def reset(self):
        self.time = self.start_time
        self.image


class button(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, name: str, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(name, True, "white").convert_alpha()
        self.rect = pygame.Rect(
            x,
            y,
            self.image.get_width() + 10,
            self.image.get_height() + 10,
        )
