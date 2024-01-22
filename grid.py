import pygame
import sys


pygame.init()



white = (255, 255, 255)
black = (0, 0, 0)

pygame.display.set_caption("Grid Example")


def draw_grid(screen, cell_size, grid_size):
    screen.fill(black)
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, white, rect, 1)