filename = "input.txt"

def part_1():
	with open(filename, "r") as f:
		answered = []
		total = 0
		for line in f.readlines():
			if line == "\n":
				total += len(answered)
				answered = []
			else:
				for c in line:
					if c != '\n' and c not in answered:
						answered.append(c)
	
	print("Part 1: ", total)
	
def part_2():
	with open(filename, "r") as f:
		answered = []
		num_pers = 0
		total = 0
		for line in f.readlines():
			if line == "\n":
				for letter in "abcdefghijklmnopqrstuvwxyz":
					if answered.count(letter) == num_pers:
						total += 1
				answered = []
				num_pers = 0
			else:
				num_pers += 1
				for c in line:
					if c != '\n':
						answered.append(c)
	
	print("Part 2: ", total)	

part_2()
