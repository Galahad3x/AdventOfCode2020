
filename_1 = "p1_input.txt"
filename_2 = "p2_input.txt"

class Deck:
	def __init__(self, starting_cards):
		self.deck = starting_cards
		
	def peek(self):
		return self.deck[0]
		
	def pop(self):
		card = self.peek()
		self.deck = self.deck[1:]
		return card
		
	def push(self, card):
		self.deck.append(card)
		
def read_input(filename):
	with open(filename, "r") as f:
		return [int(ln.rstrip('\n')) for ln in f.readlines()]
		
def play_turn(p1, p2):
	p1_card = p1.pop()
	p2_card = p2.pop()
	if p1_card > p2_card:
		print("P1 guanya ", p1_card, " a ", p2_card)
		p1.push(p1_card)
		p1.push(p2_card)
	else:
		print("P2 guanya ", p2_card, " a ", p1_card)
		p2.push(p2_card)
		p2.push(p1_card)
	print(p1.deck)
	print(p2.deck)
		
def calculate_score(p):
	score = 0
	for i in range(len(p.deck)):
		score += (p.deck[len(p.deck) - i - 1]*(i+1))
	return score
		
def part_1():
	p1 = Deck(read_input(filename_1))
	p2 = Deck(read_input(filename_2))
	print("Inicial: ", p1.deck)
	print("Inicial: ", p2.deck)
	while len(p1.deck) > 0 and len(p2.deck) > 0:
		play_turn(p1, p2)
	if len(p1.deck) > 0:
		print("P1 wins!!")
		score = calculate_score(p1)
	else:
		print("P2 wins!!")
		score = calculate_score(p2)
	print("Part 1: ", score)
	
def cr_config(p1,p2):
	return str(p1.deck) + str(p2.deck)
	
def play_turn_2(p1, p2, depth, round_c):
	print("|" * depth + " " + str(round_c))
	p1_card = p1.pop()
	p2_card = p2.pop()
	if p1_card <= len(p1.deck) and p2_card <= len(p2.deck):
		subgame_winner = play_rc_game(Deck(p1.deck[:p1_card]),Deck(p2.deck[:p2_card]), depth + 1)
		if subgame_winner == 0:
			print("P1 guanya subjoc")
			p1.push(p1_card)
			p1.push(p2_card)
		else:
			print("P2 guanya subjoc")
			p2.push(p2_card)
			p2.push(p1_card)
		return 0
	if p1_card > p2_card:
		print("P1 guanya ", p1_card, " a ", p2_card)
		p1.push(p1_card)
		p1.push(p2_card)
	else:
		print("P2 guanya ", p2_card, " a ", p1_card)
		p2.push(p2_card)
		p2.push(p1_card)
	# print(p1.deck)
	# print(p2.deck)
	
def play_rc_game(p1, p2, depth):
	configurations = []
	round_counter = 1
	while len(p1.deck) > 0 and len(p2.deck) > 0:
		conf = cr_config(p1,p2)
		if conf in configurations:
			return 0 #P1 wins
		else:
			configurations.append(conf) 
		play_turn_2(p1, p2, depth, round_counter)
		round_counter += 1
	if len(p1.deck) > 0:
		print("P1 wins!!")
		return 0 # P1 wins
	else:
		print("P2 wins!!")
		return 1 # P2 wins
	
def part_2():
	p1 = Deck(read_input(filename_1))
	p2 = Deck(read_input(filename_2))
	winner = play_rc_game(p1, p2, 1)
	if winner == 0:
		print("P1 wins!!!")
		score = calculate_score(p1)
	else:
		print("P2 wins!!!")
		score = calculate_score(p2)
	print("Part 2: ", score)
	
part_2()
