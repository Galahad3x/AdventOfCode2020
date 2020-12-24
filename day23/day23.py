import tqdm
import blist

inp = "219347865"
inp_facil = "389125467"

configs = []

class Game:
	def __init__(self, cups, current_cup, c_index):
		self.cups = blist.blist(cups)
		self.current_cup = current_cup
		self.current_cup_index = c_index

	def make_move(self):
		len_of_cups = len(self.cups)
		# print("Current cup", current_cup)
		picked_up_cups = []
		for _ in range(3):
			try:
				picked_up_cups.append(self.cups.pop((self.current_cup_index + 1) % len_of_cups))
			except IndexError:
				picked_up_cups.append(self.cups.pop(0))
		next_index = (self.current_cup_index + 1) % len(self.cups)
		next_current_cup = self.cups[next_index]
		# print("Picked up: ", picked_up_cups)
		# print("Next current ", next_current_cup)
		destination_cup = (self.current_cup - 1) % len_of_cups
		if destination_cup == 0:
			destination_cup = len_of_cups
		while destination_cup in picked_up_cups:
			destination_cup = (destination_cup - 1) % len_of_cups
			if destination_cup == 0:
				destination_cup = len_of_cups
		# print("Destination: ", destination_cup)
		dest_index = self.cups.index(destination_cup)
		for j, cup2 in enumerate(picked_up_cups):
			self.cups.insert((dest_index + j + 1) % len_of_cups, cup2)
		# print("Current ", cups)
		if dest_index > next_index:
			self.current_cup_index = next_index
		else:
			self.current_cup_index = next_index + 3
		self.current_cup = next_current_cup

class Game2:
	def __init__(self, cups, current_cup):
		self.cups = cups
		self.current_cup = current_cup

	def make_move(self):
		len_of_cups = len(self.cups)
		# print("Current cup", self.current_cup)
		picked_up_cups = []
		last_grabbed_cup = self.cups[self.current_cup]
		for _ in range(3):
			picked_up_cups.append(last_grabbed_cup)
			last_grabbed_cup = self.cups[last_grabbed_cup]
		next_current_cup = last_grabbed_cup
		# print("Picked up: ", picked_up_cups)
		# print("Next current ", next_current_cup)
		destination_cup = (self.current_cup - 1) % len_of_cups
		if destination_cup == 0:
			destination_cup = len_of_cups
		while destination_cup in picked_up_cups:
			destination_cup = (destination_cup - 1) % len_of_cups
			if destination_cup == 0:
				destination_cup = len_of_cups
		# print("Destination: ", destination_cup)
		after_destination = self.cups[destination_cup]
		last_applied_cup = destination_cup
		# print(picked_up_cups)
		for cup2 in picked_up_cups:
			self.cups[last_applied_cup] = cup2
			last_applied_cup = cup2
		# print(self.current_cup, next_current_cup)
		self.cups[self.current_cup] = next_current_cup
		self.cups[last_applied_cup] = after_destination
		# print("Current ", self.cups)
		self.current_cup = next_current_cup

def after_1(cups):
	for i, cup in enumerate(cups):
		if cup == 1:
			index_1 = i
			break
	after_1 = ""
	j = 1
	while len(after_1) < 8:
		after_1 += str(cups[(i + j) % 9])
		j += 1
	return after_1

def part_1(inp):
	cups = [int(c) for c in inp]
	current_cup = cups[0]
	print("Starting ", cups)
	for _ in range(100):
		cups = make_move(cups, current_cup)
		for i, cup in enumerate(cups):
			if cup == current_cup:
				current_cup = cups[(i + 1) % 9]
				break
	print("Final ", cups)
	print("Part 1: ", after_1(cups))
	
def two_after_1(cups):
	first_after = cups[1]
	second_after = cups[first_after]
	print(first_after, second_after)
	return first_after * second_after
	
def part_2(inp):
	cups = {}
	for i, c in enumerate(inp[:-1]):
		cups[int(c)] = int(inp[i+1])
		cup_c = int(inp[i+1])
	next_c = 10
	cups[cup_c] = next_c
	while next_c < 1000000:
		cups[next_c] = next_c + 1
		next_c += 1
	cups[1000000] = int(inp[0])
	current_cup = int(inp[0])
	# print("Starting ", cups)
	game = Game2(cups, current_cup)
	for m in tqdm.tqdm(range(10000000)):
		game.make_move()
	# print("Final ", cups)
	print("Part 2: ", two_after_1(game.cups))

	
part_2(inp)
