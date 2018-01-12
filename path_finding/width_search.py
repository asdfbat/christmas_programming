import numpy as np
import matplotlib.pyplot as plt
import imageio
import shutil
import os

def width_search(grid, start, end):
	"""
	Does a width-first path-finding search. Assumes only up/down/left/right moves, of equal weight.
	{{grid}}    = (n,m) integer array. -1 for impassable, 0 for passable, 1 for passed, 2 for current,
				   3 for start, 4 for end.
	{{start}}   = Start coordinates, array shape (2,)
	{{end}}     = Target coordinates, array shape (2,)
	{{return}}  = nr of moves, plus True/False if successful or not.
	"""
	np.save("grid.npy", grid)
	grid_size = np.shape(grid)
	moves_array = np.zeros( shape=(grid_size[0]*grid_size[1], 2), dtype=int )
	def execute_width_search():
		possible_steps = np.array([[-1,0],[0,1],[1,0],[0,-1]])
		nr_moves = 0
		end_found = False
		current_tiles = np.array([start.copy()])
		new_tiles = [0]  # Just making sure new_tiles isn't empty(see next line).
		while np.size(new_tiles) != 0:  # While not stuck.
			new_tiles = []
			for current_tile in current_tiles:  # For every former tile,
				for step in possible_steps:     # take a step in every direction.
					tile = current_tile + step
					if 0 <= tile[0] < grid_size[0] and 0 <= tile[1] < grid_size[1]\
					and grid[tile[0],tile[1]] in [0,4]:  # Checking if passable and not out of bounds.
						grid[tile[0],tile[1]] = 1  # Marking as passed.
						new_tiles.append(tile)
						nr_moves += 1
						moves_array[nr_moves] = tile
						if (tile == end).all():
							end_found = True
							print("You have arrived at your destination!")
							return(nr_moves, True)
			current_tiles = np.array(new_tiles)
		return(nr_moves, False)  # If stuck.

	nr_moves, success = execute_width_search()

	np.save("moves.npy", moves_array)
	return(grid, moves_array, nr_moves, success)