import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int, img: pygame.image) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.rect: pygame.rect.Rect = pygame.Rect(x, y, size, size)
        self.rect.center = [x, y]
        self.image: pygame.Surface = pygame.transform.scale(img, (size, size))

    def copy(self, x: int, y: int):
        return Block(x, y, self.size, self.image)

    def move(self, x: int, x_ind: int, y: int, y_ind: int) -> tuple:
        self.rect.centerx = x + x_ind * self.rect.width
        self.rect.centery = y + y_ind * self.rect.width
