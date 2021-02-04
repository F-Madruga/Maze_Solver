import time
from Drawer import Drawer, GREEN, RED, BLACK, WHITE, BLUE, YELLOW


class Dijkstra:

    def __init__(self, maze, drawer, time_per_node = 0):
        self.maze = maze
        self.drawer = drawer
        self.time_per_node = time_per_node
    
    def solve_maze(self):
        q = [(self.maze.start, [self.maze.start], 0)]
        done = set()
        while q:
            h = q[0]
            if h[0] != self.maze.start and h[0] != self.maze.goal:
                self.drawer.draw_cell(h[0], self.maze.grid, color=BLUE)
            r = q[1:]
            if h[0] == self.maze.goal:
                for node in h[1][1:-1]:
                    self.drawer.draw_cell(node, self.maze.grid, color=YELLOW)
                return h[1], h[2]
            else:
                e_filter = []
                for node in self.maze.graph[h[0]]:
                    if node not in h[1] and node not in done:
                        e_filter.append(node)
                e = [(e_final, h[1] + [e_final], h[2] + 1) for e_final in e_filter]
                done.add(h[0])
                q = sorted(e + r, key=lambda tup: (tup[2]))
            time.sleep(self.time_per_node)