filename = "input.txt"

# pos [x, y] 

N = 0 # y augmenta
E = 1 # x augmenta
S = 2 # y decreix
W = 3 # x decreix

def movs(direction):
	if direction == "N":
		return 0
	elif direction == "E":
		return 1
	elif direction == "S":
		return 2
	elif direction == "W":
		return 3
	else:
		return direction

def manhattan(xy1, xy2):
	return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def move(current_direction, current_position, movement_direction, movement_units):
	new_direction = movs(current_direction)
	new_position = current_position
	if movement_direction == "L":
		new_direction = (new_direction - (movement_units // 90)) % 4
	elif movement_direction == "R":
		new_direction = (new_direction + (movement_units // 90)) % 4
	elif movement_direction == "F":
		movement_direction = current_direction
	if movs(movement_direction) == N:
		new_position[1] += movement_units
	elif movs(movement_direction) == E:
		new_position[0] += movement_units
	elif movs(movement_direction) == S:
		new_position[1] -= movement_units
	elif movs(movement_direction) == W:
		new_position[0] -= movement_units
	return new_direction, new_position
	

def part_1():
	direction = E
	pos = [0, 0]
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			movement_direction = line[0]
			movement_units = int(line[1:])
			direction, pos = move(direction, pos, movement_direction, movement_units)
	print("Part 1: ", manhattan(pos, (0, 0)))

def rotate_waypoint_on_zero(current_waypoint, direction, quarters):
	for _ in range(quarters):
		current_waypoint[0], current_waypoint[1] = current_waypoint[1], current_waypoint[0]
		if direction == "L":
			current_waypoint[0] *= -1
		if direction == "R":
			current_waypoint[1] *= -1
	return current_waypoint
	
def rotate_waypoint(position, current_waypoint, direction, quarters):
	modified = [w - position[i] for i, w in enumerate(current_waypoint)]
	rotated = rotate_waypoint_on_zero(modified, direction, quarters)
	return [w + position[i] for i, w in enumerate(rotated)]

def move_forward(new_direction, new_position, new_waypoint, current_position, current_waypoint,
movement_units):
	if current_waypoint[1] > current_position[1]:
		movement = (current_waypoint[1] - current_position[1]) * movement_units
		_, new_position = move(new_direction,
					new_position,
					"N",
					movement)
		_, new_waypoint = move(new_direction,
					new_waypoint,
					"N",
					movement)
	elif current_waypoint[1] < current_position[1]:
		movement = (current_position[1] - current_waypoint[1]) * movement_units
		_, new_position = move(new_direction,
					new_position,
					"S",
					movement)
		_, new_waypoint = move(new_direction,
					new_waypoint,
					"S",
					movement)
	if current_waypoint[0] > current_position[0]:
		movement = (current_waypoint[0] - current_position[0]) * movement_units
		_, new_position = move(new_direction,
					new_position,
					"E",
					movement)
		_, new_waypoint = move(new_direction,
					new_waypoint,
					"E",
					movement)
	elif current_waypoint[0] < current_position[0]:
		movement = (current_position[0] - current_waypoint[0]) * movement_units
		_, new_position = move(new_direction,
					new_position,
					"W",
					movement)
		_, new_waypoint = move(new_direction,
					new_waypoint,
					"W",
					movement)
	return new_direction, new_position, new_waypoint

def move_2(current_waypoint, current_direction, current_position, movement_direction, movement_units):
	print("Current: ", current_direction, current_position, movement_direction, movement_units, current_waypoint)
	new_direction = movs(current_direction)
	new_position = current_position
	new_waypoint = current_waypoint
	if movement_direction == "L":
		new_direction = (new_direction - (movement_units // 90)) % 4
		new_waypoint = rotate_waypoint(current_position, new_waypoint, "L", (movement_units // 90) % 4)
	elif movement_direction == "R":
		new_direction = (new_direction + (movement_units // 90)) % 4
		new_waypoint = rotate_waypoint(current_position, new_waypoint, "R", (movement_units // 90) % 4)
	elif movement_direction == "F":
		new_direction, new_position, new_waypoint = move_forward(new_direction,
										new_position,
										new_waypoint,
										current_position,
										current_waypoint,
										movement_units)
	if movs(movement_direction) == N:
		new_waypoint[1] += movement_units
	elif movs(movement_direction) == E:
		new_waypoint[0] += movement_units
	elif movs(movement_direction) == S:
		new_waypoint[1] -= movement_units
	elif movs(movement_direction) == W:
		new_waypoint[0] -= movement_units
	print("New: ", new_direction, new_position, new_waypoint)
	return new_direction, new_position, new_waypoint

def part_2():
	direction = E
	pos = [0, 0]
	waypoint = [10, 1]
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			movement_direction = line[0]
			movement_units = int(line[1:])
			direction, pos, waypoint = move_2(waypoint,
								direction,
								pos,
								movement_direction,
								movement_units)
			# xs = input("Next step...")
	print("Part 1: ", manhattan(pos, (0, 0)))

part_2()
