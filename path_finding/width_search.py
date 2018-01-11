import numpy as np
import matplotlib.pyplot as plt
import imageio

grid_size = (100,100)
start = np.array( [np.random.randint(grid_size[0]//4), np.random.randint(grid_size[1]//4)] )
target = np.array( [np.random.randint(3*grid_size[0]//4, grid_size[0]),\
				    np.random.randint(3*grid_size[1]//4, grid_size[1])] )
grid = np.random.choice([-1,0], size=grid_size, p=[0.3,0.7])  # -1 for impassable, 0 for passable,
grid[target[0],target[1]] = 2  			  					# 1 for already passed.
grid[start[0],start[1]] = -2
grid_weights = np.zeros(grid_size)  # Too be filled with grid weights. 0 means unpassed.
grid_weights[start[0],start[1]] = 0
possible_steps = np.array([[-1,0],[0,1],[1,0],[0,-1]])

plt.matshow(grid)
plt.savefig("fig/plot_00000.png")
plt.close()


def x():
	moves = 0
	target_found = False
	current_tiles = np.array([start.copy()])
	new_tiles = [0,0]
	while np.size(new_tiles) != 0:  # Checking if stuck.
		new_tiles = []
		for current_tile in current_tiles:  # For every former tile,
			for step in possible_steps:     # take a step in every direction.
				tile = current_tile + step
				if 0 <= tile[0] < grid_size[0] and 0 <= tile[1] < grid_size[1]\
				and grid[tile[0],tile[1]] in [0,2]:  # Checking if passable and not passed
									   			     # and not out of bounds.
					grid_weights[tile[0],tile[1]] = grid_weights[current_tile[0],current_tile[1]] + 1
					grid[tile[0],tile[1]] = 1
					new_tiles.append(tile)

					plt.matshow(grid)
					moves += 1
					plt.savefig("fig/plot_%.5d.png"%moves)
					plt.close()
					if (tile == target).all():
						target_found = True
						print("target_found")
						return(moves)
		current_tiles = np.array(new_tiles)
	return(0)

moves = x()

#images = []
#for i in range(1, moves):
#	images.append( imageio.imread("fig/plot_%d.png"%i) )
#imageio.mimsave("movie.gif", images)