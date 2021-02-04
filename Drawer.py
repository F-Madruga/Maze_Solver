import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)

class Drawer:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_cell(self, cell, grid, color=WHITE, border_color=BLACK):
        grid_width, grid_height = grid.shape
        cell_width = self.width / grid_width
        cell_height = self.height / grid_height
        rect = pygame.Rect(cell[0] * cell_width, cell[1] * cell_height, cell_width, cell_height)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, border_color, rect, 1)
        pygame.display.update()