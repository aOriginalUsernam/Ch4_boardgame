import pygame


class Board:
    def __init__(
        self, color: pygame.color.Color, left: int, top: int, width: int, height: int
    ):
        self.color = color
        rgb = [color.r, color.g, color.b]
        if color.r < 235:
            rgb[0] = color.r + 15
        if color.g > 5:
            rgb[1] = color.g - 5
        if color.b > 5:
            rgb[2] = color.b - 5
        self.next_shape_color = pygame.Color(rgb)
        self.tot_board = pygame.Rect(left, top, width, height)
        self.next_shape_board = pygame.Rect(left, height - width, width, height)

    def draw(self, screen: pygame.surface):
        pygame.draw.rect(screen, self.color, self.tot_board)
        pygame.draw.rect(screen, self.next_shape_color, self.next_shape_board)

    def is_xpos_in_board(self, x: int) -> bool:
        return self.tot_board.left <= x and self.tot_board.right >= x
