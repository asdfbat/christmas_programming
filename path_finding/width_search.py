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
	moves_list_broad = []
	possible_steps = np.array([[-1,0],[0,1],[1,0],[0,-1]])
	def execute_width_search():
		end_found = False
		current_tiles = np.array([start.copy()])
		new_tiles = [0]  # Just making sure new_tiles isn't empty(see next line).
		nr_moves = 0
		while np.size(new_tiles) != 0:  # While not stuck.
			new_tiles = []
			for current_tile in current_tiles:  # For every former tile,
				for step in possible_steps:     # take a step in every direction.
					tile = current_tile + step
					if 0 <= tile[0] < grid_size[0] and 0 <= tile[1] < grid_size[1]\
					and grid[tile[0],tile[1]] in [0,4]:  # Checking if passable and not out of bounds.
						if (tile == end).all():
							end_found = True
							print("You have arrived at your destination!")
							return(nr_moves, True)
						new_tiles.append(tile)
						nr_moves += 1
						grid[tile[0],tile[1]] = 1  # Marking as passed.
						moves_array[nr_moves-1] = tile
			current_tiles = np.array(new_tiles)
			moves_list_broad.append(current_tiles)
		return(nr_moves, False)  # If stuck.
	nr_moves, success = execute_width_search()
	moves_array = moves_array[:nr_moves]
	shortest_path = []
	current_tile = end
	for i in range(len(moves_list_broad)-1, -1, -1):
		for tile in moves_list_broad[i]:
			for possible_step in current_tile + possible_steps:
				if (tile == possible_step).all():
					shortest_path.append(tile)
					current_tile = tile
					break
	shortest_path = np.array(shortest_path)
	np.save("moves.npy", moves_array)
	np.save("shortest_path.npy", shortest_path)
	np.save("path_broad.npy", moves_list_broad)
	return(grid, moves_array, nr_moves, success)