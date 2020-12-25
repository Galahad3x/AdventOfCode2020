from tqdm import tqdm

card_public_key = 19774466
door_public_key = 7290641

def do_loop(subject_number, value=1):
	value *= subject_number
	return value % 20201227

def part_1():
	value = 1
	subject = 7
	card_loop_size = 0
	while value != card_public_key:
		value = do_loop(subject, value)
		card_loop_size += 1
	door_loop_size = 0
	value = 1
	subject = 7
	while value != door_public_key:
		value = do_loop(subject, value)
		door_loop_size += 1
	print("Card loop size: ", card_loop_size)
	print("Door loop size: ", door_loop_size)
	key = 1
	subject = door_public_key
	for _ in tqdm(range(card_loop_size)):
		key = do_loop(subject, key)
	print("Part 1: ", key)

part_1()
