from block import Block
import pygame


class Shape(pygame.sprite.Group):
    def __init__(self, list_2d: list[list[Block]]) -> None:
        self.list_2d = list_2d
        list_1d = []
        for sprites in list_2d:
            list_1d.extend(sprites)
        pygame.sprite.Group.__init__(self, list_1d)
        self.x = list_2d[0][-1].rect.x - list_2d[0][0].rect.x
        self.y = list_2d[-1][0].rect.y - list_2d[0][0].rect.y
