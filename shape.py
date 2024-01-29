from block import Block
import pygame
from shapes import Shapes
from grid import *


class Shape(pygame.sprite.Group):
    def __init__(self, block: Block, shape: Shapes, rotate) -> None:
        self.shape = shape
        self.block = block
        self.list_2d = self.create_shape(block, rotate)
        list_1d = []
        for row in self.list_2d:
            for sprite in row:
                if sprite is not None:
                    list_1d.append(sprite)
        pygame.sprite.Group.__init__(self, list_1d)
        self.is_placed = False

    def create_shape(self, block: Block, rotate = False):
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
                if rotate:
                    self.shape = Shapes.ONEBYTWO
                    return self.create_shape(block)

                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                ]
            case Shapes.TWOBYTWO:
                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [block.copy(x, y + width), block.copy(x + width, y + width)],
                ]
            case Shapes.ONEBYTWO:
                if rotate:
                    self.shape = Shapes.TWOBYONE
                    return self.create_shape(block)

                return [
                    [block.copy(x, width + y)],
                    [block.copy(x, y)],
                ]
            case Shapes.S_BLOCK:
                if rotate:
                    self.shape = Shapes.S_BLOCK_R
                    return self.create_shape(block)

                return [
                    [None, block.copy(width + x, y), block.copy(width * 2 + x, y)],
                    [
                        block.copy(width + x, y + width),
                        block.copy(x, y + width),
                    ],
                ]
            case Shapes.S_BLOCK_R:
                if rotate:
                    self.shape = Shapes.S_BLOCK
                    return self.create_shape(block)

                return [
                    [block.copy(x, y), None],
                    [block.copy(x, width + y), block.copy(width + x, width + y)],
                    [None, block.copy(width + x, 2*width + y)
                     ],
                    ]
            case Shapes.Z_BLOCK:
                if rotate:
                    self.shape = Shapes.Z_BLOCK_R
                    return self.create_shape(block)

                return [
                    [block.copy(x, y), block.copy(width + x, y)],
                    [
                        None,
                        block.copy(width + x, y + width),
                        block.copy(2 * width + x, y + width),
                    ],
                ]

            case Shapes.Z_BLOCK_R:
                if rotate:
                    self.shape = Shapes.Z_BLOCK
                    return self.create_shape(block)

                return [
                    [None, block.copy(width + x, y)],
                    [block.copy(x, width + y), block.copy(width + x, width + y)],
                    [block.copy(x, 2*width + y), None
                     ],
                    ]

            case Shapes.I_BLOCK_LYING:
                if rotate:
                    self.shape = Shapes.I_BLOCK_STANDING
                    return self.create_shape(block)

                return [
                    [
                        block.copy(x, y),
                        block.copy(width + x, y),
                        block.copy(2 * width + x, y),
                        block.copy(3 * width + x, y),
                    ]
                ]
            case Shapes.I_BLOCK_STANDING:
                if rotate:
                    self.shape = Shapes.I_BLOCK_LYING
                    return self.create_shape(block)

                return [
                    [block.copy(x, y)],
                    [block.copy(x, y + width)],
                    [block.copy(x, y + 2 * width)],
                    [block.copy(x, y + 3 * width)],
                ]

            case Shapes.T_BLOCK:
                if rotate:
                    self.shape = Shapes.T_BLOCK_R
                    return self.create_shape(block)

                return [
                    [None, block.copy(width + x, y), None],
                    [block.copy(x, width + y), block.copy(width + x, width + y), block.copy(2*width + x, width + y)]
                ]
            
            case Shapes.T_BLOCK_R:
                if rotate:
                    self.shape = Shapes.T_BLOCK_R2
                    return self.create_shape(block)

                return [
                    [None, block.copy(width + x, y)],
                    [block.copy(x, width + y), block.copy(width + x, width + y)],
                    [None, block.copy(width + x, 2*width + y)]
                ]
            
            case Shapes.T_BLOCK_R2:
                if rotate:
                    self.shape = Shapes.T_BLOCK_R3
                    return self.create_shape(block)

                return [
                    [block.copy(x, y), block.copy(width + x, y), block.copy(2*width + x, y)],
                    [None, block.copy(width + x, width + y)]
                ]

            case Shapes.T_BLOCK_R3:
                if rotate:
                    self.shape = Shapes.T_BLOCK
                    return self.create_shape(block)

                return [
                    [block.copy(x, y), None],
                    [block.copy(x, width + y), block.copy(width + x, width + y)],
                    [block.copy(x, 2*width + y), None]
                ]

            case _:
                raise ValueError(Shapes)

    def move(self, x: int, y: int) -> None:
        if self.is_placed:
            return
        add_y = 0
        for row in self.list_2d:
            add_x = 0
            for block in row:
                if block is not None:
                    block.move(x, add_x, y, add_y)
                add_x += 1
            add_y += 1
