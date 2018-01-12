"""
Generates a random grid if passable/impassable tiles for the width_search
Random start and target locations.
"""
import numpy as np
from width_search import width_search

grid_size = (20,20)
start = np.array( [np.random.randint(grid_size[0]//4), np.random.randint(grid_size[1]//4)] )
target = np.array( [np.random.randint(3*grid_size[0]//4, grid_size[0]),\
				    np.random.randint(3*grid_size[1]//4, grid_size[1])] )
grid = np.random.choice([-1,0], size=grid_size, p=[0.3,0.7])
grid[target[0],target[1]] = 2
grid[start[0],start[1]] = -2
grid_weights = np.zeros(grid_size)

moves, success = width_search(grid, True)
