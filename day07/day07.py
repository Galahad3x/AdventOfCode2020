filename = "input.txt"

def read_rules_1():
	rls = {}
	with open(filename,"r") as f:
		for line in f.readlines():
			spl = line.split(" contain ")
			color = spl[0][:-5] # eliminar el bags
			rls[color] = []
			for cl in spl[1].split(","):
				if cl.strip().split(" ")[0] != "no":
					rls[color].append(" ".join(cl.strip().split(" ")[1:3]))
	return rls
			

def part_1():
	rules = read_rules_1()
	print(rules)
	able_colors = []
	for key in rules.keys():
		if "shiny gold" in rules[key]:
			able_colors.append(key)
	print(able_colors)
	modified = 1
	while modified == 1:
		modified = 0
		for key in rules.keys():
			for color in able_colors:
				if color in rules[key] and key not in able_colors:
					able_colors.append(key)
					modified = 1
		print(able_colors)
	print("Part 1: ", len(able_colors))
	
def read_rules_2():
	rls = {}
	with open(filename,"r") as f:
		for line in f.readlines():
			spl = line.split(" contain ")
			color = spl[0][:-5] # eliminar el bags
			rls[color] = []
			for cl in spl[1].split(","):
				if cl.strip().split(" ")[0] != "no":
					for _ in range(int(cl.strip().split(" ")[0])):
						rls[color].append(" ".join(cl.strip().split(" ")[1:3]))
	return rls
			
def get_no_of_bags(rules, color):
	if rules[color] == []:
		return 0
	else:
		return sum([(1 + get_no_of_bags(rules, cl)) for cl in rules[color]])

def part_2():
	rules = read_rules_2()
	print(rules)
	print("Part 2: ", get_no_of_bags(rules, "shiny gold"))
	
part_2()
