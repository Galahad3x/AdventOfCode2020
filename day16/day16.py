from functools import reduce

rules_filename = "rules_input.txt"
my_ticket_filename = "my_ticket_input.txt"
nearby_filename = "nearby_input.txt"

def read_rules():
	rules = {}
	with open(rules_filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			spl = line.split(": ")
			rule_name = spl[0]
			ranges_txt = spl[1].split(" or ")
			ranges = []
			for rang in ranges_txt:
				ranges.append([int(r) for r in rang.split("-")])
			rules[rule_name] = ranges

	return rules
		
def valid_line(line, rules):
	retval = 0
	for field in [int(f) for f in line.split(",")]:
		some_rule = False
		for rule in rules.keys():
			ranges = rules[rule]
			if (field >= ranges[0][0] and field <= ranges[0][1]) or \
				(field >= ranges[1][0] and field <= ranges[1][1]):
				some_rule = True
		if not some_rule:
			retval += field
	return retval
	


def part_1():
	rules = read_rules()
	ticket_scanning_error_rate = 0
	with open(nearby_filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			ticket_scanning_error_rate += valid_line(line, rules)
			
	print("Part 1: ", ticket_scanning_error_rate)
	
def in_range(field, rule_ranges):
	if (field >= rule_ranges[0][0] and field <= rule_ranges[0][1]) or \
		(field >= rule_ranges[1][0] and field <= rule_ranges[1][1]):
		return True
	return False
	
def part_2():
	rules = read_rules()
	indexes = {}
	for key in rules.keys():
		indexes[key] = []
	tickets = []
	definitive_indexes = {}
	with open(nearby_filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			if valid_line(line, rules) == 0:
				tickets.append([int(f) for f in line.split(",")])
	for i in range(len(tickets[0])):
		for key in rules.keys():
			valid = True
			for ticket in tickets:
				if not in_range(ticket[i], rules[key]):
					valid = False
			if valid:
				indexes[key].append(i)
	while len(definitive_indexes.keys()) < len(rules.keys()):
		for rule in indexes.keys():
			if len(indexes[rule]) == 1:
				definitive_indexes[rule] = indexes[rule][0]
				for rule2 in indexes.keys():
					if definitive_indexes[rule] in indexes[rule2]:
						indexes[rule2].remove(definitive_indexes[rule])
				del indexes[rule]
				break
	my_ticket = [int(n) for n in open(my_ticket_filename, "r").read().rstrip('\n').split(",")]
	departure_values = []
	for rule in definitive_indexes.keys():
		if rule.startswith("departure"):
			departure_values.append(my_ticket[definitive_indexes[rule]])
			
	print("Part 2: ", reduce((lambda x, y: x * y), departure_values))	
	
part_2()
