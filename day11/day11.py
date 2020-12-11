from functools import reduce

filename = "input.txt"

def read_input():
	seats = []
	with open(filename, "r") as f:
		for line in f.readlines():
			ln = line.rstrip('\n')
			seats.append(ln)
	return seats
	
def occupied_adjacents(seats, i, j):
	adjacents = [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]
	count = 0
	for adjacent in adjacents:
		if adjacent[0] >= 0 and adjacent[0] < len(seats):
			if adjacent[1] >= 0 and adjacent[1] < len(seats[adjacent[0]]):
				if seats[adjacent[0]][adjacent[1]] == "#":
					count += 1
	return count
	
def n_of_seats(seats):
	return sum([ln.count("#") for ln in seats])
	
def simulate_step(old_seats):
	news = []
	for i, line in enumerate(old_seats):
		new_l = []
		for j, seat in enumerate(line):
			if seat == ".":
				new_l.append(".")
			elif seat == "L":
				if occupied_adjacents(old_seats, i, j) == 0:
					new_l.append("#")
				else:
					new_l.append("L")
			elif seat == "#":
				if occupied_adjacents(old_seats, i, j) >= 4:
					new_l.append("L")
				else:
					new_l.append("#")
		news.append(new_l[:])
	return news
	
def part_1():
	old_seats = read_input()
	new_seats = simulate_step(old_seats)
	while new_seats != old_seats:
		old_seats = new_seats
		new_seats = simulate_step(old_seats)
	print("Part 1: ", n_of_seats(new_seats))
	return n_of_seats(new_seats)

def occupied_seen(seats, i, j):
	distance = 1
	adjacents = [(i+distance,j),(i-distance,j),(i,j+distance),(i,j-distance),(i+distance,j+distance),(i-distance,j-distance),(i+distance,j-distance),(i-distance,j+distance)]
	done = [False] * 8
	count = 0
	while reduce((lambda x, y: x and y), done) == False:
		for x in range(len(done)):
			if done[x] == False:
				if adjacents[x][0] >= 0 and adjacents[x][0] < len(seats):
					if adjacents[x][1] >= 0 and adjacents[x][1] < len(seats[adjacents[x][0]]):
						if seats[adjacents[x][0]][adjacents[x][1]] == ".":
							continue
						elif seats[adjacents[x][0]][adjacents[x][1]] == "#":
							count += 1
				done[x] = True
		distance += 1
		adjacents = [(i+distance,j),(i-distance,j),(i,j+distance),(i,j-distance),(i+distance,j+distance),(i-distance,j-distance),(i+distance,j-distance),(i-distance,j+distance)]
	return count

def simulate_step_2(old_seats):
	news = []
	for i, line in enumerate(old_seats):
		new_l = []
		for j, seat in enumerate(line):
			if seat == ".":
				new_l.append(".")
			elif seat == "L":
				if occupied_seen(old_seats, i, j) == 0:
					new_l.append("#")
				else:
					new_l.append("L")
			elif seat == "#":
				if occupied_seen(old_seats, i, j) >= 5:
					new_l.append("L")
				else:
					new_l.append("#")
		news.append(new_l[:])
	return news

def part_2():
	old_seats = read_input()
	new_seats = simulate_step_2(old_seats)
	while new_seats != old_seats:
		old_seats = new_seats
		new_seats = simulate_step_2(old_seats)
	print("Part 2: ", n_of_seats(new_seats))
	return n_of_seats(new_seats)


part_2()
