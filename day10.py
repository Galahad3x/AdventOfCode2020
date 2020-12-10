from itertools import combinations
from functools import reduce

filename = "input10.txt"

def read_input():
	ins = []
	with open(filename, "r") as f:
		for line in f.readlines():
			ln = line.rstrip('\n')
			ins.append(int(ln))
	return ins

def part_1():
	values = read_input()
	values.sort()
	prev_value = 0
	difs_1 = 0
	difs_3 = 1
	for value in values:
		if value - prev_value == 1:
			difs_1 += 1
		elif value - prev_value == 3:
			difs_3 += 1
		prev_value = value
	print("Part 1: ", difs_1 * difs_3)
	
def is_valid(comb, start, end):
	if len(comb) == 0:
		print("Comb ", [start] + list(comb) + [end], end - start == 1 or end - start == 2 or end - start == 3)
		return end - start == 1 or end - start == 2 or end - start == 3
	prev_value = start
	for value in list(comb) + [end]:
		if value - prev_value == 1 or value - prev_value == 2 or value - prev_value == 3:
			prev_value = value
		else:
			print("Comb ", [start] + list(comb) + [end], " fals")
			return False
	print("Comb ", [start] + list(comb) + [end], " true")
	return True

def find_arrangements(ran):
	print("Ran: ", ran)
	if len(ran) == 1 or len(ran) == 2:
		print("Possibles: 1")
		return 1
	if len(ran) == 3:
		if ran[-1] - ran[0] == 1 or ran[-1] - ran[0] == 2 or ran[-1] - ran[0] == 3:
			print("Possibles: ", 2)
			return 2
		else:
			print("Possibles: 1")
			return 1
	possibles = 1 # Tots seguits
	for i in range(len(ran) - 2):
		for comb in combinations(ran[1:-1], i):
			print(comb, end=",")
			if is_valid(comb, ran[0], ran[-1]):
				possibles += 1
	print("Possibles: ", possibles)
	return possibles
		
		
	
def part_2():
	values = read_input()
	values.append(0)
	values.sort()
	print(values)
	values.append(values[-1] + 3)
	print(values)
	possible_combs = []
	prev_value = 0
	current_range = []
	for value in values:
		if value - prev_value < 3:
			current_range.append(value)
		else:
			possible_combs.append(find_arrangements(current_range))
			current_range = [value]
		prev_value = value
	print(possible_combs)
	print("Part 2: ", reduce((lambda x, y: x* y), possible_combs))
	
part_2()
