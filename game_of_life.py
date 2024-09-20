from os import system, name
from time import sleep
import random as rnd
import patterns

# Conway's Game of Life

# Rules:
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def clear_console():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For macOS and Linux
    else:
        _ = system('clear')
 
def print_grid(grid):
    for row in grid:
        print(*row)



alive = "■"
dead = "."
cols = 120
rows = 60

grid = [[dead for _ in range(cols)] for _ in range(rows)]

for _ in range(20):
    patterns.add_random_pattern(grid)


# main loop
while True:
    clear_console()
    print_grid(grid)

    new_grid = [[dead for _ in range(cols)] for _ in range(rows)]

    for i in range(len(grid)-1,-1,-1):
        for j in range(len(grid[i])):
      
            # get alive cell neighbour count
            neighbours = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    
                    ni, nj = i+x, j+y
                    
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]): # boundary detection
                        neighbours.append(grid[ni][nj])

            alive_neighbours = neighbours.count(alive)
            
            
            # game rules
            if grid[i][j] == alive:
                if alive_neighbours < 2 or alive_neighbours > 3:
                    new_grid[i][j] = dead
                else:
                    new_grid[i][j] = alive
            else:
                if alive_neighbours == 3:
                    new_grid[i][j] = alive
                else:
                    new_grid[i][j] = dead
                
    grid = new_grid.copy()
    sleep(0.2)