from block import Block
import pygame
from shapes import Shapes
from grid import *


class Shape(pygame.sprite.Group):
    def __init__(self, block: Block, shape: Shapes) -> None:
        self.shape = shape
        self.list_2d = self.create_shape(block)
        list_1d = []
        for row in self.list_2d:
            for sprite in row:
                if sprite is not None:
                    list_1d.append(sprite)
        pygame.sprite.Group.__init__(self, list_1d)

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
            case Shapes.ONEBYTWO:
                return [
                    [block.copy(x, width + y)],
                    [block.copy(x, y)],
                ]
            case Shapes.S_BLOCK:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [
                        None,
                        block.copy(width + x, y + width),
                        block.copy(2 * width + x, y + width),
                    ],
                ]
            case Shapes.Z_BLOCK:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [
                        None,
                        block.copy(width + x, y + width),
                        block.copy(2 * width + x, y + width),
                    ],
                ]
            case Shapes.I_BLOCK_LYING:
                return [
                    [
                        block.copy(x, y),
                        block.copy(width + x, y),
                        block.copy(2 * width + x, y),
                        block.copy(3 * width + x, y),
                    ]
                ]
            case Shapes.I_BLOCK_STANDING:
                return [
                    [block.copy(x, y)],
                    [block.copy(x, y + width)],
                    [block.copy(x, y + 2 * width)],
                    [block.copy(x, y + 3 * width)],
                ]
            case _:
                raise ValueError(Shapes)

    def move(self, x: int, y: int):
        add_y = 0
        for row in self.list_2d:
            add_x = 0
            for block in row:
                if block is not None:
                    block.move(x, add_x, y, add_y)
                add_x += 1
            add_y += 1
