import pygame
import sys


pygame.init()



white = (255, 255, 255)
black = (0, 0, 0)




def draw_grid(screen, cell_size, grid_size):
    screen.fill(black)
    for row in range(grid_size):
        for column in range(grid_size):
            rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, white, rect, 1)