from PIL import Image
import numpy as np
from Drawer import Drawer, GREEN, RED, BLACK, WHITE


class Maze:

    def __init__(self, image, drawer):
        self.drawer = drawer
        self.grid = np.array(image)
        self.width = self.grid.shape[0]
        self.height = self.grid.shape[1]
        self.start = None
        self.goal = None
        self.graph = self.__generate_graph()
        

    def __str__(self):
        return str(self.width) + " x " + str(self.height) + "\n\n" + str(self.grid)

    def __generate_graph(self):
        g = {}
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x, y] == 1:
                    g[(x, y)] = self.__get_neighbours(x, y)
                    if (x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1):
                        if self.start == None:
                            self.start = (x, y)
                            self.drawer.draw_cell((x, y), self.grid, color=GREEN)
                        else:
                            self.goal = (x, y)
                            self.drawer.draw_cell((x, y), self.grid, color=RED)
                    else:
                        self.drawer.draw_cell((x, y), self.grid)
                else:
                    self.drawer.draw_cell((x, y), self.grid, color=BLACK)
        return g

    def __get_neighbours(self, x, y):
        possible_neighbours = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y -1)]
        neighbours = set()
        for p_neighbour in possible_neighbours:
            if p_neighbour[0] >= 0 and p_neighbour[0] < self.width and \
            p_neighbour[1] >= 0 and p_neighbour[1] < self.height and \
            self.grid[p_neighbour[0], p_neighbour[1]] == 1:
                neighbours.add(p_neighbour)
        return neighbours