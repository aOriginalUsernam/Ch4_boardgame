from block import Block
import pygame
from shapes import Shapes


class Shape(pygame.sprite.Group):
    def __init__(self, block: Block, shape: Shapes) -> None:
        self.shape = shape
        self.list_2d = self.create_shape(block)
        list_1d = []
        for sprites in self.list_2d:
            list_1d.extend(sprites)
        pygame.sprite.Group.__init__(self, list_1d)
        self.x = self.list_2d[0][-1].rect.x - self.list_2d[0][0].rect.x
        self.y = self.list_2d[-1][0].rect.y - self.list_2d[0][0].rect.y

    def create_shape(self, block: Block):
        x = block.rect.x
        y = block.rect.y
        width = block.rect.width
        match self.shape:
            case Shapes.ONEBYONE:
                return [
                    [
                        block.copy(x, y),
                    ],
                ]
            case Shapes.TWOBYONE:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                ]
            case Shapes.TWOBYTWO:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [block.copy(x, y + width), block.copy(x + width, y + width)],
                ]
            case _:
                raise ValueError(Shapes)

    def move(self, x: int, y: int):
        add_y = 0
        for row in self.list_2d:
            add_x = 0
            for block in row:
                block.move(x, add_x, y, add_y)
                add_x += 1
            add_y += 1
