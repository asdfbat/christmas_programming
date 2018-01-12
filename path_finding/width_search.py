import numpy as np
import matplotlib.pyplot as plt
import imageio
import shutil
import os
import time

def width_search(grid, savegif=True, keepfigs=False):
	"""
	Does a width-first path-finding search. Assumes only up/down/left/right moves, of equal weight.
	{{grid}}      = (n,m) integer array. -1 for imassable, 0 for passable, 1 for passed, 2 for target, -2 for start.
	{{savegif}}   = True/False, save a gif of all the moves.
	{{keepfigs}}  = True/False, keep the images needed to create gif.
	{{return}}    = nr of moves, plus True/False if successful or not.
	"""

	def execute_width_search():
		possible_steps = np.array([[-1,0],[0,1],[1,0],[0,-1]])
		grid_size = np.shape(grid)
		moves = 0
		target_found = False
		current_tiles = np.array([start.copy()])
		new_tiles = [0]  # Just making sure new_tiles isn't empty(see next line).
		while np.size(new_tiles) != 0:  # While not stuck.
			new_tiles = []
			for current_tile in current_tiles:  # For every former tile,
				for step in possible_steps:     # take a step in every direction.
					tile = current_tile + step
					if 0 <= tile[0] < grid_size[0] and 0 <= tile[1] < grid_size[1]\
					and grid[tile[0],tile[1]] in [0,2]:  # Checking if passable and not out of bounds.
						grid_weights[tile[0],tile[1]] = grid_weights[current_tile[0],current_tile[1]] + 1
						grid[tile[0],tile[1]] = 1  # Marking as passed.
						new_tiles.append(tile)
						moves += 1
						if savegif:
							plt.matshow(grid)
							plt.savefig("fig/plot_%.5d.png"%moves)
							plt.close()
						if (tile == target).all():
							target_found = True
							print("target found!")
							return(moves, True)
			current_tiles = np.array(new_tiles)
		return(moves, False)  # If stuck.

	if savegif:
		current_path = os.path.dirname(os.path.realpath(__file__))
		fig_path = os.path.join(current_path, "fig")
		if not os.path.exists(fig_path):
			os.makedirs(fig_path)
		plt.matshow(grid)
		plt.savefig("fig/plot_00000.png")
		plt.close()

	moves, success = execute_width_search()
	if savegif:
		images = []
		for i in range(moves+1):
			images.append( imageio.imread("fig/plot_%.5d.png"%i) )
		imageio.mimsave("movie.gif", images)

	if not keepfigs and savegif:
		shutil.rmtree(fig_path)

	return(moves, success)