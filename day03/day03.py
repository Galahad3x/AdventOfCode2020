from functools import reduce

filename = "input.txt"

slope_map = []
with open(filename, "r") as f:
	for line in f.readlines():
		if line[-1] == '\n':
			slope_map.append(line[:-1])	

def calculate_slope(slope):
	currents = [0, 0]
	trees = 0

	print(len(slope_map), len(slope_map[0]))

	while currents[0] < len(slope_map):
		print(currents)
		if slope_map[currents[0]][currents[1]] == '#':
			print("Tree")
			trees += 1
		currents[0] += slope[0]
		currents[1] = (currents[1] + slope[1]) % len(slope_map[1])
		
	try:
		if slope_map[currents[0]][currents[1]] == '#':
			trees += 1
	except IndexError:
		pass
		
	return trees
	
print("Part 1: ", calculate_slope((1,3)))

answers = []
slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

for slope in slopes:
	answers.append(calculate_slope(slope))
	
answer = reduce((lambda x, y: x * y), answers)

print("Part 2: ", answer)
