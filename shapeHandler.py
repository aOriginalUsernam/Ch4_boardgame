from shapes import Shapes
from shape import Shape
from block import Block
import random
import pygame.surface


class ShapeHandler:
    def __init__(self) -> None:
        self.all_shapes: list[Shape] = []
        self.current_shape = -1

    def generate_shape(self, block: Block) -> Shape:
        toReturn = Shape(block, Shapes(random.randint(0, 7)))
        # toReturn = Shape(block, Shapes.I_BLOCK_STANDING)
        self.all_shapes.append(toReturn)
        self.current_shape += 1
        return toReturn

    def draw_shapes(self, screen: pygame.surface):
        for shape in self.all_shapes:
            shape.draw(screen)
