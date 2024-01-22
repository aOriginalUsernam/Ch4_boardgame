from block import Block
import pygame
from shapes import Shapes


class Shape(pygame.sprite.Group):
    def __init__(self, block: Block, shape: Shapes) -> None:
        self.list_2d = self.create_shape(shape, block)
        list_1d = []
        for sprites in self.list_2d:
            list_1d.extend(sprites)
        pygame.sprite.Group.__init__(self, list_1d)
        self.x = self.list_2d[0][-1].rect.x - self.list_2d[0][0].rect.x
        self.y = self.list_2d[-1][0].rect.y - self.list_2d[0][0].rect.y

    def create_shape(self, shape, block: Block):
        x = block.rect.x
        y = block.rect.y
        width = block.rect.width
        match shape:
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
            case Shapes.ONEBYTWO:
                return [
                    [block.copy(x, width + y)],
                    [block.copy(x, y)],
                ]
            case Shapes.S_BLOCK:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [block.copy(width + x, y - width), block.copy(2*width + x, y - width)],
                ]
            case Shapes.Z_BLOCK:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [block.copy(width + x, y + width), block.copy(2*width + x, y + width)],
                ]
            case Shapes.I_BLOCK_LYING:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [block.copy(2*width + x, y), block.copy(3*width + x, y)],
                    ]
            case Shapes.I_BLOCK_STANDING:
                return [
                    [block.copy(x, y), block.copy(x, y - width)],
                    [block.copy(x, y - 2*width), block.copy(x, y - 3*width)],
                ]
            case _:
                raise ValueError(Shapes)
