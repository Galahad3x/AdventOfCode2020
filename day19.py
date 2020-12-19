import itertools

rules_filename = "rules_input.txt"
msg_filename = "msg_input.txt"

def read_rules():
	rules = {}
	with open(rules_filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			spl = line.split(": ")
			rule_no = int(spl[0])
			rules[rule_no] = []
			for rule in spl[1].split(" | "):
				try:
					rules[rule_no].append([int(s) for s in rule.split(" ")])
				except ValueError:
					rules[rule_no] = rule[1]
	# print(rules)
	return rules

def create_expression(index, rules):
	# print("Index: ", index, " Regla: ", rules[index])
	if type(rules[index]) == str:
		return rules[index]
	possibles = []
	for possible_rule in rules[index]:
		possibles_in_rule = [""]
		# print(possible_rule) # [n1, n2, ...]
		for elem in possible_rule:
			ex = create_expression(elem, rules)
			# print("Ex: ", ex)
			if type(ex) == str:
				for i in range(len(possibles_in_rule)):
					possibles_in_rule[i] += ex
			else:
				new_possibles = []
				for elem2 in possibles_in_rule:
					for ex_elem in ex:
						# print("Exelem: ", ex_elem)
						for ex_f in ex_elem:
							new_possibles.append(elem2 + ex_f)
				possibles_in_rule = new_possibles
			# print(possibles_in_rule)
		possibles.append(possibles_in_rule)
		# print("Index: ", index, "Possibles: ", possibles)
	return possibles
			
			
def part_1():
	rules = read_rules()
	expression = create_expression(0, rules)
	# print(expression[0])
	cont = 0
	with open(msg_filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			if line in expression[0]:
				cont += 1
	print("Part 1: ", cont)
	
def create_expression_2(index, rules, max_deep, current_deep):
	# print("Index: ", index, " Regla: ", rules[index])
	if type(rules[index]) == str:
		return rules[index]
	if current_deep >= max_deep:
		return "a"
	possibles = []
	for possible_rule in rules[index]:
		possibles_in_rule = [""]
		# print(possible_rule) # [n1, n2, ...]
		for elem in possible_rule:
			ex = create_expression_2(elem, rules, max_deep, current_deep + 1)
			# print("Ex: ", ex)
			if type(ex) == str:
				for i in range(len(possibles_in_rule)):
					possibles_in_rule[i] += ex
			else:
				new_possibles = []
				for elem2 in possibles_in_rule:
					for ex_elem in ex:
						# print("Exelem: ", ex_elem)
						for ex_f in ex_elem:
							new_possibles.append(elem2 + ex_f)
				possibles_in_rule = new_possibles
			# print(possibles_in_rule)
		possibles.append(possibles_in_rule)
		# print("Index: ", index, "Possibles: ", possibles)
	return possibles

class Grammar:
	def __init__(self, rules):
		self.rules = rules
		self.results = {}
		
	def is_accepted(self, word):
		return self._is_accepted(word, 0)
		
	def _is_accepted(self, word, index):
		# print(index, word)
		if word in self.results:
			if index in self.results[word]:
				# print("Found")
				return self.results[word][index]
		if type(self.rules[index]) == str:
			return self.rules[index] == word
		for possible_rule in self.rules[index]:
			# print(possible_rule) # [n1, n2, ...]
			if len(possible_rule) == 1:
				if self._is_accepted(word, possible_rule[0]):
					if word in self.results:
						self.results[word][index] = True
					else:
						self.results[word] = {index: True}
					return True
			if len(possible_rule) == 2:
				for i in range(1, len(word)): # [:i] es el primer
					if self._is_accepted(word[:i], possible_rule[0]) and \
						self._is_accepted(word[i:], possible_rule[1]):
						if word in self.results:
							self.results[word][index] = True
						else:
							self.results[word] = {index: True}
						return True
			if len(possible_rule) == 3:
				for i in range(1, len(word)): # [:i] es el primer
					for j in range(1, len(word)):
						if j >= i:
							if self._is_accepted(word[:i], possible_rule[0]):
								if self._is_accepted(word[i:j], possible_rule[1]):
									if self._is_accepted(word[j:], possible_rule[2]):
										if word in self.results:
											self.results[word][index] = True
										else:
											self.results[word] = {index: True}
										return True
		if word in self.results:
			self.results[word][index] = False
		else:
			self.results[word] = {index: False}
		return False
		

def part_2():
	rules = read_rules() # 8: [[42]]
	rules[8] = [[42],[42,8]]
	rules[11] = [[42, 31], [42, 11, 31]]
	gram = Grammar(rules)
	cont = 0
	with open(msg_filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			print(line)
			if gram.is_accepted(line):
				print("accepted")
				cont += 1
	print("Part 2: ", cont)
	

part_2()


