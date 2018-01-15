import numpy as np
from grid_animator import grid_animator

grid_size = (120,120)
portal_grid = np.zeros((grid_size[0], grid_size[1],2), dtype=int)
grid = np.zeros((grid_size[0], grid_size[1]), dtype=int)
start = np.array([0,0])
end = np.array([grid_size[0]-1, grid_size[1]-1])
possible_steps = np.array([[-1,0], [0,1], [1,0], [0,-1]])

portal_grid[end[0],end[1]] = (-1,-1)
portal_grid[0,0] = (-2,-2)
grid[end[0],end[1]] = 4
grid[0,0] = 3

inverse_portals_grid = np.zeros((grid_size[0], grid_size[1],2), dtype=int)

with open("test_portals.txt", "r") as infile:
	for line in infile:
		in_portal, out_portal = line.split("->")
		in_portal = eval(in_portal)
		out_portal = eval(out_portal)
		portal_grid[in_portal] = out_portal
		grid[in_portal] = 5
		grid[out_portal] = 6
		inverse_portals_grid[out_portal] = in_portal

np.save("grid.npy", grid)

def portal_search(grid, portal_grid, start, end):
	moves_list_broad = []
	moves_array = []

	def execute_portal_search():
		nr_moves = 0
		current_tiles = np.array([start.copy()])
		target_found = False
		while target_found == False:
			new_tiles = []
			for current_tile in current_tiles:
				for step in possible_steps:
					tile = current_tile + step
					if 0 <= tile[0] < grid_size[0] and 0 <= tile[1] < grid_size[1] and grid[tile[0],tile[1]] in [0,5,4]:
						if (portal_grid[tile[0],tile[1]] != np.array([0,0])).all():  # Either found target or a portal.
							if (portal_grid[tile[0],tile[1]] == np.array([-1,-1])).all():  # Found target.
								target_found = True
								print("Search Successful after %d moves!" % nr_moves)
								return(nr_moves, True)
							else:  # Found portal.
								tile = portal_grid[tile[0],tile[1]]
						grid[tile[0],tile[1]] = 1  # Marking as passed.
						new_tiles.append(tile)
						moves_array.append(tile)
			nr_moves += 1
			current_tiles = np.array(new_tiles)
			moves_list_broad.append(current_tiles)
		print("Search Failed after %d moves!" % nr_moves)
		return(nr_moves, False)

	nr_moves, success = execute_portal_search()

	shortest_path = []
	current_tile = end.copy()
	for i in range(len(moves_list_broad)-1, -1, -1):
		for tile in moves_list_broad[i]:
			found_one = False
			for possible_tile in current_tile + possible_steps:
				if (tile == possible_tile).all():
					shortest_path.append(tile)
					current_tile = tile
					found_one = True
					break
			for possible_tile in inverse_portals_grid[current_tile[0],current_tile[1]] + possible_steps:
				if (tile == possible_tile).all() and found_one == False\
				and (inverse_portals_grid[current_tile[0],current_tile[1]] != np.array([0,0])).all():
					shortest_path.append(tile)
					current_tile = tile
					break




	shortest_path = np.array(shortest_path)
	np.save("moves.npy", moves_array)
	np.save("moves_broad.npy", moves_list_broad)
	np.save("portal_grid.npy", portal_grid)
	np.save("shortest_path.npy", shortest_path)

portal_search(grid, portal_grid, start, end)

grid_animator(reserved_numbers=[3,4,5,6])