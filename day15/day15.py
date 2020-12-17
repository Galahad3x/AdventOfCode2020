filename = "input.txt"

def part_1():
	with open(filename, "r") as f:
		starters = [int(n) for n in f.readline().split(",")]
	turn = 0
	most_recent = {}
	second_recent = {}
	last_spoken = 0
	while turn < 2020:
		if turn < len(starters):
			most_recent[starters[turn]] = turn
			last_spoken = starters[turn]
			turn += 1
			continue
		if last_spoken not in second_recent:
			second_recent[0] = most_recent[0]
			most_recent[0] = turn
			last_spoken = 0
		else:
			last_spoken = most_recent[last_spoken] - second_recent[last_spoken]
			if last_spoken in most_recent:
				second_recent[last_spoken] = most_recent[last_spoken]
			most_recent[last_spoken] = turn
		turn += 1
	print("Part 1: ", last_spoken)
	
def part_2():
	with open(filename, "r") as f:
		starters = [int(n) for n in f.readline().split(",")]
	turn = 0
	most_recent = {}
	second_recent = {}
	last_spoken = 0
	while turn < 30000000:
		if turn % 10000 == 0:
			print(turn)
		if turn < len(starters):
			most_recent[starters[turn]] = turn
			last_spoken = starters[turn]
			turn += 1
			continue
		if last_spoken not in second_recent:
			second_recent[0] = most_recent[0]
			most_recent[0] = turn
			last_spoken = 0
		else:
			last_spoken = most_recent[last_spoken] - second_recent[last_spoken]
			if last_spoken in most_recent:
				second_recent[last_spoken] = most_recent[last_spoken]
			most_recent[last_spoken] = turn
		turn += 1
	print("Part 2: ", last_spoken)

part_2()
