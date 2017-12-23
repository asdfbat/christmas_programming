import numpy as np
import operator

loc = (24,24)
grid = np.zeros((48,48))
grid[loc] = 1

with open("path.txt", "r") as infile:
    for line in infile:
        length, direction = line.split()
        length = int(length[:-1])
        if direction == "north":
            direction = (0,1)
        elif direction == "south":
            direction = (0,-1)
        elif direction == "east":
            direction = (1,0)
        elif direction == "west":
            direction = (-1,0)
        else:
            raise ValueError("Direction ", direction, " is not defined")
        for i in range(1, length+1):
            loc = tuple(map(operator.add, loc, direction))
            grid[loc] += 1
            print(grid[loc])

string = ""
for row in grid:
    for row_element in row:
        if row_element != 0:
            string += "* "
        else:
            string += "  "
    print(string)
    string = ""
