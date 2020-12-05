filename = "input.txt"

def calculate_row(chars):
	start = [0,128]
	for char in chars:
		if char == "F":
			start[1] = start[0] + ((start[1] - start[0]) // 2)
		elif char == "B":
			start[0] = start[0] + ((start[1] - start[0]) // 2)
	print(start)
	return start[0]
	
def calculate_seat(chars):
	start = [0,8]
	for char in chars:
		if char == "L":
			start[1] = start[0] + ((start[1] - start[0]) // 2)
		elif char == "R":
			start[0] = start[0] + ((start[1] - start[0]) // 2)
	print(start)
	return start[0]

def part_1():
	max_id = 0
	with open(filename,"r") as f:
		for line in f.readlines():
			val = calculate_row(line[:7]) * 8 + calculate_seat(line[7:])
			if val > max_id:
				max_id = val
	print("Part 1: ", max_id)
	
def part_2():
	ids = []
	with open(filename,"r") as f:
		for line in f.readlines():
			val = calculate_row(line[:7]) * 8 + calculate_seat(line[7:])
			ids.append(val)
	not_found = 0
	for i in range(908):
		if i not in ids:
			not_found = i
			print(i)
	print("Part 2: ", not_found)
	
part_2()
