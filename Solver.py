import timeit, pygame, sys
from Maze import Maze
from Dijkstra import Dijkstra
from AStar import AStar
from PIL import Image
from Drawer import Drawer, BLACK


def main():
    image_path = "./examples/braid200.png"
    time = 0
    image = Image.open(image_path)

    drawer = Drawer(1040, 1040)
    drawer.screen.fill(BLACK)
    pygame.init()

    maze_loaded = False
    solved = False

    maze = None
    
    while True:

        if not maze_loaded:
            print("Loading maze from image...")
            start = timeit.default_timer()
            maze = Maze(image, drawer)
            time_elapsed =  timeit.default_timer() - start
            print("Time loading maze: ", round(time_elapsed, 2))
            maze_loaded = True
        
        if not solved:

            print("Start: ", maze.start)
            print("Goal: ", maze.goal)
            print("Solving maze...")
            
            a_star = AStar(maze, drawer,time_per_node=time)
            #dijkstra = Dijkstra(maze, drawer, time_per_node=time)
            
            start = timeit.default_timer()
            
            path, cost = a_star.solve_maze()
            #path, cost = dijkstra.solve_maze()
            
            time_elapsed =  timeit.default_timer() - start
            print("Time to solve maze: ", round(time_elapsed, 2))
            print("Cost: ", cost)
            solved = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()
