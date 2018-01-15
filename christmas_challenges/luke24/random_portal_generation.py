import random
size = 120
nr_portals = 40

with open("test_portals.txt", "w") as outfile:
	for i in range(nr_portals):
		portal_in = (random.randint(0,size-1), random.randint(0,size-1))
		portal_out = (random.randint(0,size-1), random.randint(0,size-1))
		outfile.write(str(portal_in) + " -> " + str(portal_out) + "\n")