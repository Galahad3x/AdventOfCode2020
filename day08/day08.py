filename = "input.txt"

class Instruction:
	def __init__(self, instruction, value):
		self.instruction = instruction
		self.value = value
		self.has_been_run = False
		
	def run(self, accumulator, instruction_counter):
		self.has_been_run = True
		if self.instruction == "acc":
			accumulator += self.value
			instruction_counter += 1
		elif self.instruction == "jmp":
			instruction_counter += self.value
		elif self.instruction == "nop":
			instruction_counter += 1
		return accumulator, instruction_counter
		
def get_ops():
	ops = []
	with open(filename, "r") as f:
		for line in f.readlines():
			spl = line.split(" ")
			ins = Instruction(spl[0], int(spl[1]))
			ops.append(ins)
	return ops
	
def part_1():
	ops = get_ops()
	accumulator = instruction_counter = 0
	current_op = ops[instruction_counter]
	while not current_op.has_been_run:
		accumulator, instruction_counter = current_op.run(accumulator, instruction_counter)
		current_op = ops[instruction_counter]
	print("Part 1: ", accumulator)
	
def run_all(ops):
	accumulator = instruction_counter = 0
	current_op = ops[instruction_counter]
	while not current_op.has_been_run and instruction_counter < len(ops):
		accumulator, instruction_counter = current_op.run(accumulator, instruction_counter)
		if instruction_counter < len(ops):		
			current_op = ops[instruction_counter]
		else:
			break
	if instruction_counter < len(ops):
		# print("Infinite loop")
		pass
	else:
		# print("Finished correctly")
		print("Part 2: ", accumulator)

def find_negative_jmps(ops):
	return [i for i, op in enumerate(ops) if op.instruction == "jmp" and op.value < 0]

def part_2():
	ops = get_ops()
	negs = find_negative_jmps(ops)
	for neg in negs:
		ops[neg].instruction = "nop"
		run_all(ops)
		ops = get_ops()
	

part_2()
