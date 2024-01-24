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
        self.is_placed = False

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
                    [None, block.copy(width + x , y), block.copy(width*2 + x, y)],
                    [
                        block.copy(width + x, y + width),
                        block.copy(x, y + width),
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

    def check_is_valid_pos(self, x, y, shape, width_and_height, cell_size): # niet vergeten indexes anders te schrijven later want als je een groter bord opgeeft werkt het niet
        closest_index = 0
        match shape:
            case Shapes.ONEBYONE:
                return True

            case Shapes.TWOBYONE:
                return not x >= 205 + width_and_height * cell_size
            
            case Shapes.TWOBYTWO:
                return not (x >= 205 + width_and_height * cell_size or y >= 205 + width_and_height * cell_size)

            case Shapes.ONEBYTWO:
                return not y >= 205 + width_and_height * cell_size

            case Shapes.S_BLOCK:
                return not (x >= 205 + width_and_height * cell_size - cell_size or y >= 205 + width_and_height * cell_size)

            case Shapes.Z_BLOCK:
                return not (x >= 205 + width_and_height * cell_size - cell_size or y >= 205 + width_and_height * cell_size)

            case Shapes.I_BLOCK_LYING:
                return not (x >= 205 + width_and_height * cell_size - 2*cell_size)
            
            case Shapes.I_BLOCK_STANDING:
                return not (y >= 205 + width_and_height * cell_size - 2*cell_size)
            
            
            
            # elif shape == Shapes.S_BLOCK and closest_index in (90,91,92,93,94,95,96,97,8,18,28,38,48,58,68,78,88,98,9,19,29,39,49,59,69,79,89,99):
            #     return False
            
            # elif shape == Shapes.Z_BLOCK and x >= width_and_height * cell_size + 3*cell_size or y == 255 + width_and_height * cell_size - cell_size:
            #     return False
        return True