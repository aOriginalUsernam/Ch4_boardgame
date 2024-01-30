import pygame
from shapes import Shapes
from shapeHandler import ShapeHandler


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
            self.image = self.font.render(f"{self.time} seconds", True, "white")

    def reset(self):
        self.time = self.start_time
        self.image


class Button(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, name: str, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(name, True, "white").convert_alpha()
        self.rect = pygame.Rect(
            x,
            y,
            self.image.get_width() + 10,
            self.image.get_height() + 10,
        )


class Image(pygame.sprite.Sprite):
    def __init__(self, image: pygame.image, x: int, y: int, size: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = pygame.Rect(
            x,
            y,
            self.image.get_width() + 10,
            self.image.get_height() + 10,
        )

    def rotate_block(self, shape, block):
        shape = None
        match block:
            case Shapes.ONEBYONE:
                return

            case Shapes.TWOBYONE:
                shape = Shapes.ONEBYTWO
        ShapeHandler.generate_shape(block, shape)


class Points(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, points: int, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(points), True, "white").convert_alpha()
        self.rect = pygame.Rect(
            x,
            y,
            self.image.get_width() + 10,
            self.image.get_height() + 10,
        )
        self.points = points
        self.font = font

    def add_points(self, shape: Shapes, density: int):
        match shape:
            case Shapes.ONEBYONE:
                self.points += 1

            case Shapes.TWOBYONE:
                if density <= 70:
                    self.points += 1
                else:
                    self.points += 2

            case Shapes.TWOBYTWO:
                if density <= 50:
                    self.points += 2
                elif density <= 70:
                    self.points += 3
                else:
                    self.points += 4

            case Shapes.ONEBYTWO:
                if density <= 70:
                    self.points += 1
                else:
                    self.points += 2

            case Shapes.S_BLOCK:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.S_BLOCK_R:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.Z_BLOCK:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.Z_BLOCK_R:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.I_BLOCK_LYING:
                if density <= 80:
                    self.points += 2
                else:
                    self.points += 3

            case Shapes.I_BLOCK_STANDING:
                if density <= 80:
                    self.points += 2
                else:
                    self.points += 3

            case Shapes.T_BLOCK:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.T_BLOCK_R:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.T_BLOCK_R2:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

            case Shapes.T_BLOCK_R3:
                if density <= 30:
                    self.points += 2
                elif density <= 50:
                    self.points += 3
                elif density <= 70:
                    self.points += 4
                else:
                    self.points += 5

        self.image = self.font.render(f"{self.points}", True, "white")
        return self.points
