import pygame
import sys


class Grid:
    def __init__(self, cell_size, cell_amount, margin) -> None:
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.cell_centers = []
        self.cell_size = cell_size
        self.cell_amount = cell_amount
        self.margin = margin

    def draw_grid(self, screen):
        screen.fill(self.black)
        cell_centers = []

        for row in range(self.cell_amount):
            for column in range(self.cell_amount):
                rect = pygame.Rect(
                    column * self.cell_size + self.margin,
                    row * self.cell_size + self.margin,
                    self.cell_size,
                    self.cell_size,
                )

                pygame.draw.rect(screen, self.white, rect, 1)

                center_x = rect.centerx
                center_y = rect.centery

                cell_centers.append((center_x, center_y))

        self.cell_centers = cell_centers

    def closest_grid(self, mouse_x, mouse_y):
        distances = [
            ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
            for x, y in self.cell_centers
        ]
        closest_index = distances.index(min(distances))

        return self.cell_centers[closest_index], closest_index
