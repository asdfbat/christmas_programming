import numpy as np
import matplotlib.pyplot as plt
import imageio
import shutil
import os

def grid_animator():
	current_path = os.path.dirname(os.path.realpath(__file__))
	fig_path = os.path.join(current_path, "fig")
	if not os.path.exists(fig_path):
		os.makedirs(fig_path)

	grid = np.load("grid.npy")
	moves_array = np.load("moves.npy")
	actual_path = np.load("path.npy")
	grid_size = np.shape(grid)
	nr_moves = len(moves_array)
	plt.matshow(grid)
	plt.savefig("fig/plot_00000.png")
	plt.close()

	for move_count, move in enumerate(moves_array):
		grid[move[0],move[1]] = 2
		plt.matshow(grid)
		plt.savefig("fig/plot_%.5d.png"%(move_count+1))
		plt.close()
		grid[move[0],move[1]] = 1

	for i in range(len(actual_path)):
		grid[actual_path[i,0],actual_path[i,1]] = 2
	plt.matshow(grid)
	plt.savefig("fig/plot_%.5d.png"%(nr_moves+1))
	plt.close()

	images = []
	for i in range(nr_moves+1):
		images.append( imageio.imread("fig/plot_%.5d.png"%i) )
	for i in range(10):  # Adding multiple of last img to make it stay longer.
		images.append( imageio.imread("fig/plot_%.5d.png"%(nr_moves+1)))
	imageio.mimsave("movie.gif", images)

	shutil.rmtree(fig_path)

if __name__ == "__main__":
	grid_animator()