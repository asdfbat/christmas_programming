"""
Generates a random grid if passable/impassable tiles for the width_search
Random start and end locations.
"""
import numpy as np
from width_search import width_search
from grid_animator import grid_animator

grid_size = (24,24)
start = np.array( [np.random.randint(grid_size[0]//4), np.random.randint(grid_size[1]//4)] )
end = np.array( [np.random.randint(3*grid_size[0]//4, grid_size[0]),\
				    np.random.randint(3*grid_size[1]//4, grid_size[1])] )
grid = np.random.choice([-1,0], size=grid_size, p=[0.3,0.7])
grid[start[0],start[1]] = 3
grid[end[0],end[1]] = 4

width_search(grid, start, end)
grid_animator(moves_filename="path_broad.npy")