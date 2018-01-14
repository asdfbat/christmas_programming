grid = zeros(Int16, 10,10)
for i in 1:10, j in 1:10
	if rand() > 0.7
		grid[i,j] = 1
	end
end

beginning = [2, 2]
target = Int16[9, 9]
println(target)
grid[2,2] = 4
grid[9,9] = 5
println(grid)

legal_moves = Int16[-1 0 1  0;
					 0 1 0 -1]

new_tiles = zeros(Int16, 2, 30)  # "Long enough" array, to be filled with the next tiles.
current_tiles = zeros(Int16, 2, 30)
current_tiles[:,1] = beginning
new_tiles[:,1] = [-1,-1]
nr_moves = 0
nr_current_tiles = 1
while current_tiles[:,1] != [0,0]
	nr_new_tiles = 0
	for i in 1:size(legal_moves,2)
		for j in 1:nr_current_tiles
			tile = legal_moves[:,i] + current_tiles[:,j]
			if 0 < tile[1] <= 10 && 0 < tile[2] <= 10 && grid[tile[1],tile[2]] in [0 5]
				nr_moves += 1
				nr_new_tiles += 1
				new_tiles[:, nr_new_tiles] = tile
				grid[tile[1],tile[2]] = 2
				println("new tile ", tile)
				if tile == target
					println("Search Successful after $nr_moves moves!")
				end
			end
		end
	end
	current_tiles = copy(new_tiles)
	new_tiles[:] = 0
	nr_current_tiles = nr_new_tiles
end