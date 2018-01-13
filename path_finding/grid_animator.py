import numpy as np
import matplotlib.pyplot as plt
import imageio
import shutil
import os

def grid_animator(grid_filename="grid.npy", moves_filename="moves.npy",\
				shortest_path_filename="shortest_path.npy", delete_img=True):
	"""
	Animating a path-finding algorithm on a square board. Reads numpy-arrays from file.
	{{grid.npy}}  = (n,m) start board. -1 for unpassable, 0 for passable, 3 for start, 4 for target.
	{{moves.npy}} = (x,2) or (x,y,2). Former shows every tile-search seperately, in order.
					Latter shows searches of (y) moves at a time. (y) can vary through the search.
	{{shortest_path.npy}}  = (z,2). Tiles included in shortest path. Displayed at the end.
	"""

	current_path = os.path.dirname(os.path.realpath(__file__))
	fig_path = os.path.join(current_path, "fig")
	if not os.path.exists(fig_path):
		os.makedirs(fig_path)

	grid = np.load(grid_filename)
	moves_array = np.load(moves_filename)
	shortest_path = np.load(shortest_path_filename)
	grid_size = np.shape(grid)
	nr_moves = len(moves_array)
	plt.matshow(grid)
	plt.savefig("fig/plot_00000.png")
	plt.close()

	for move_count, move in enumerate(moves_array):
		if np.shape(move) == (2,):
			grid[move[0],move[1]] = 2
		else:
			for sub_move in move:
				grid[sub_move[0],sub_move[1]] = 2
		plt.matshow(grid)
		plt.savefig("fig/plot_%.5d.png"%(move_count+1))
		plt.close()
		if np.shape(move) == (2,):
			grid[move[0],move[1]] = 1
		else:
			for sub_move in move:
				grid[sub_move[0],sub_move[1]] = 1

	for i in range(len(shortest_path)):
		grid[shortest_path[i,0],shortest_path[i,1]] = 2
	plt.matshow(grid)
	plt.savefig("fig/plot_%.5d.png"%(nr_moves+1))
	plt.close()

	images = []
	for i in range(nr_moves+1):
		images.append( imageio.imread("fig/plot_%.5d.png"%i) )
	for i in range(10):  # Adding multiple of last img to make it stay longer.
		images.append( imageio.imread("fig/plot_%.5d.png"%(nr_moves+1)))
	imageio.mimsave("movie.gif", images)

	if delete_img:
		shutil.rmtree(fig_path)

if __name__ == "__main__":
	grid_animator()