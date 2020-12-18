filename = "input.txt"

def solve_line(line):
	print(line)
	res = 0
	parenthesis = 0
	parenthesis_line = ""
	last_operation = "+"
	for c in line:
		# print("C", c, "Line: ", parenthesis_line, parenthesis_line != "", parenthesis)
		if parenthesis == 0:
			if parenthesis_line != "":
				if last_operation == "+":
					res += solve_line(parenthesis_line)
				else:
					res *= solve_line(parenthesis_line)
				parenthesis_line = ""
			if c in "123456789":
				if last_operation == "+":
					res += int(c)
				else:
					res *= int(c)
			else:
				if c not in "()":
					last_operation = c
				elif c == "(":
					parenthesis += 1
				elif c == ")":
					parenthesis -= 1
		else:
			if c == "(":
				parenthesis += 1
			if c == ")":
				parenthesis -= 1
			if parenthesis == 0 and c == ")":
				continue
			parenthesis_line += c
	if parenthesis_line != "":
		if last_operation == "+":
			res += solve_line(parenthesis_line)
		else:
			res *= solve_line(parenthesis_line)
	return res
		
def part_1():
	res = 0
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			res += solve_line(line.replace(" ",""))
	print("Part 1: ", res)

def add_parenthesis(line):
	sumes = line.count("+")
	for i in range(sumes):
		pendents = i
		for i, c in enumerate(line):
			if c == "+":
				if pendents > 0:
					pendents -= 1
					print("+ at ", i , " ignored")
				else:
					parentesis_flag = 0
					esq = 0
					dre = len(line)
					for j, ch in list(enumerate(line))[i-1::-1]:
						if parentesis_flag == 0 and ch in "123456789":
							esq = j
							break
						else:
							if ch == ")":
								parentesis_flag += 1
							elif ch == "(":
								parentesis_flag -= 1
							if parentesis_flag == 0:
								esq = j
								break
					parentesis_flag = 0
					for j, ch in list(enumerate(line))[i+1:]:
						if parentesis_flag == 0 and ch in "123456789":
							dre = j
							break
						else:
							if ch == "(":
								parentesis_flag += 1
							elif ch == ")":
								parentesis_flag -= 1
							if parentesis_flag == 0:
								dre = j
								break
					line = line[:esq] + "(" + line[esq:dre+1] + ")" + line[dre+1:]
					print("Edit: ", line)
					break
	return line
				

def part_2():
	res = 0
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			res += solve_line(add_parenthesis(line.replace(" ","")))
	print("Part 2: ", res)


part_2()
