from shapes import Shapes
from shape import Shape
from block import Block
import random
import pygame.surface


class ShapeHandler:
    def __init__(self, blocks: dict[Block]) -> None:
        self.blocks = blocks
        self.all_shapes: list[Shape] = []
        self.current_shape = -1
        self.covered_cells = set()

    def generate_shape(self, block: Block, shape=None, rotate=None) -> Shape:
        if shape is None:
            toReturn = Shape(block, Shapes(random.randint(0, 6)), rotate)
        else:
            toReturn = Shape(block, shape, rotate)

        self.all_shapes.append(toReturn)
        self.current_shape += 1
        return toReturn

    def draw_shapes(self, screen: pygame.surface):
        for shape in self.all_shapes:
            shape.draw(screen)

    def check_is_valid_pos(
        self,
        x: int,
        y: int,
        shape,
        width_and_height,
        cell_size,
        closest_index,
    ):
        # get closest index of shape
        match shape:
            case Shapes.ONEBYONE:
                if closest_index in self.covered_cells:
                    return False
                else:
                    self.covered_cells.add(closest_index)
                    return True

            case Shapes.TWOBYONE:
                if (
                    closest_index in self.covered_cells
                    or closest_index + 1 in self.covered_cells
                ):
                    return False
                else:
                    result = not x >= 205 + width_and_height * cell_size
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + 1)

                return result

            case Shapes.TWOBYTWO:
                if (
                    closest_index in self.covered_cells
                    or closest_index + 1 in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size
                        or y >= 205 + width_and_height * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)

                return result

            case Shapes.ONEBYTWO:
                if (
                    closest_index in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                ):
                    return False
                else:
                    result = not y >= 205 + width_and_height * cell_size
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + width_and_height)

                return result

            case Shapes.S_BLOCK:
                if (
                    closest_index + 1 in self.covered_cells
                    or closest_index + 2 in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size - cell_size
                        or y >= 205 + width_and_height * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + 2)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)

                return result

            case Shapes.S_BLOCK_R:
                if (
                    closest_index in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                    or closest_index + 2 * width_and_height + 1 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size
                        or y >= 205 + width_and_height * cell_size - cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)
                        self.covered_cells.add(closest_index + 2 * width_and_height + 1)

                return result

            case Shapes.Z_BLOCK:
                if (
                    closest_index in self.covered_cells
                    or closest_index + 1 in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                    or closest_index + width_and_height + 2 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size - cell_size
                        or y >= 205 + width_and_height * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + width_and_height + 1)
                        self.covered_cells.add(closest_index + width_and_height + 2)

                return result

            case Shapes.Z_BLOCK_R:
                if (
                    closest_index + 1 in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                    or closest_index + 2 * width_and_height in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size
                        or y >= 205 + width_and_height * cell_size - cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)
                        self.covered_cells.add(closest_index + 2 * width_and_height)

                return result

            case Shapes.I_BLOCK_LYING:
                if (
                    closest_index in self.covered_cells
                    or closest_index + 1 in self.covered_cells
                    or closest_index + 2 in self.covered_cells
                    or closest_index + 3 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size - 2 * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + 2)
                        self.covered_cells.add(closest_index + 3)

                return result

            case Shapes.I_BLOCK_STANDING:
                if (
                    closest_index in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + 2 * width_and_height in self.covered_cells
                    or closest_index + 3 * width_and_height in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        y >= 205 + width_and_height * cell_size - 2 * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + 2 * width_and_height)
                        self.covered_cells.add(closest_index + 3 * width_and_height)

                return result

            case Shapes.T_BLOCK:
                if (
                    closest_index + 1 in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                    or closest_index + width_and_height + 2 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size - cell_size
                        or y >= 205 + width_and_height * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)
                        self.covered_cells.add(closest_index + width_and_height + 2)

                return result

            case Shapes.T_BLOCK_R:
                if (
                    closest_index + 1 in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                    or closest_index + 2 * width_and_height + 1 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size
                        or y >= 205 + width_and_height * cell_size - cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)
                        self.covered_cells.add(closest_index + 2 * width_and_height + 1)

                return result

            case Shapes.T_BLOCK_R2:
                if (
                    closest_index in self.covered_cells
                    or closest_index + 1 in self.covered_cells
                    or closest_index + 2 in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size - cell_size
                        or y >= 205 + width_and_height * cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + 1)
                        self.covered_cells.add(closest_index + 2)
                        self.covered_cells.add(closest_index + width_and_height + 1)

                return result

            case Shapes.T_BLOCK_R3:
                if (
                    closest_index in self.covered_cells
                    or closest_index + width_and_height in self.covered_cells
                    or closest_index + width_and_height + 1 in self.covered_cells
                    or closest_index + 2 * width_and_height in self.covered_cells
                ):
                    return False
                else:
                    result = not (
                        x >= 205 + width_and_height * cell_size
                        or y >= 205 + width_and_height * cell_size - cell_size
                    )
                    if result:
                        self.covered_cells.add(closest_index)
                        self.covered_cells.add(closest_index + width_and_height)
                        self.covered_cells.add(closest_index + width_and_height + 1)
                        self.covered_cells.add(closest_index + 2 * width_and_height)

                return result

        return True
