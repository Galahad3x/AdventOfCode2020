from copy import deepcopy

filename = "input.txt"

def read_input():
	ingredients = []
	allergens = {}
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n').rstrip(')') for ln in f.readlines()]:
			spl = line.split("(contains ")
			ingredients_in_line = spl[0].split(" ")
			ingredients_in_line.remove("")
			for allergen in spl[1].split(", "):
				if allergen in allergens:
					allergens[allergen].append(ingredients_in_line)
				else:
					allergens[allergen] = [ingredients_in_line]
			for ing in ingredients_in_line:
				ingredients.append(ing)
	return ingredients, allergens

def part_1():
	ingredients, allergens = read_input()
	definitive_allergens = {}
	not_determined = {}
	for allergen in allergens.keys():
		print("Allergen: ", allergen)
		possible_containers = allergens[allergen][0]
		print("Possible containers: ", possible_containers)
		print("Allergens: ", allergens[allergen][1:])
		for l in allergens[allergen][1:]:
			new_possibles = possible_containers[:]
			for elem in possible_containers:
				print("Elem: ", elem)
				if elem not in l:
					print("Removing ", elem)
					new_possibles.remove(elem)
			possible_containers = new_possibles
		if len(possible_containers) == 1:
			print("Found ", allergen, ": ", possible_containers[0])
			definitive_allergens[allergen] = possible_containers[0]
		else:
			not_determined[allergen] = possible_containers
	old_not_det = []
	while len(not_determined) > 0:
		new_not_determined = deepcopy(not_determined)
		old_not_det = list(not_determined.values())
		for allergen in not_determined.keys():
			for ingredient in definitive_allergens.values():
				if ingredient in not_determined[allergen]:
					not_determined[allergen].remove(ingredient)
			if len(not_determined[allergen]) == 1:
				print("Found ", allergen, ": ", not_determined[allergen][0])
				definitive_allergens[allergen] = not_determined[allergen][0]
				del new_not_determined[allergen]
		if old_not_det == list(not_determined.values()):
			break
		print(old_not_det, not_determined.values())
		old_not_det = list(not_determined.values())
		not_determined = new_not_determined
	print(definitive_allergens)
	print(not_determined)
	for sure_has_allergen in definitive_allergens.values():
		ingredients = [ing for ing in ingredients if ing != sure_has_allergen]
	for sure_has_allergen in not_determined.values():
		for allr in sure_has_allergen:
			ingredients = [ing for ing in ingredients if ing != allr]
	print("Part 1: ", len(ingredients))
	return definitive_allergens, not_determined
	
def generate_canonical_dangerous_list(defs):
	in_list = [(key,defs[key]) for key in defs.keys()]
	in_list.sort()
	return ",".join([t[1] for t in in_list])
	
def part_2():
	defs, nds = part_1()
	while len(nds) > 0:
		for found_allergen in defs:
			for not_f_allergen in nds:
				if defs[found_allergen] in nds[not_f_allergen]:
					nds[not_f_allergen].remove(defs[found_allergen])
		ks = list(nds.keys())
		for key in ks:
			if len(nds[key]) == 1:
				defs[key] = nds[key][0]
				del nds[key]
			elif len(nds[key]) == 0:
				del nds[key]
	print(defs)
	print("Part 2: ")
	print(generate_canonical_dangerous_list(defs))
	
part_2()
