import pygame
import sys


pygame.init()



white = (255, 255, 255)
black = (0, 0, 0)




def draw_grid(screen, cell_size, grid_size, margin):
    screen.fill(black)
    cell_centers = []

    for row in range(grid_size):
        for column in range(grid_size):
            rect = pygame.Rect(column * cell_size + margin, row * cell_size + margin, cell_size, cell_size)

            pygame.draw.rect(screen, white, rect, 1)

            center_x = rect.centerx
            center_y = rect.centery

            cell_centers.append((center_x, center_y))

    return cell_centers


def closest_grid(cell_centers, mouse_x, mouse_y):
    distances = [((mouse_x - x)**2 + (mouse_y - y)**2)**0.5 for x, y in cell_centers]
    closest_index = distances.index(min(distances))

    return cell_centers[closest_index]