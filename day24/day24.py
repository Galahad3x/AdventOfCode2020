# https://www.redblobgames.com/grids/hexagons/
from tqdm import tqdm
from blist import blist

filename = "input.txt"

class Tile:
	def __init__(self, position, white=True):
		self.position = position
		self.white = white
		
	def flip(self):
		self.white = not self.white
		
def part_1():
	tiles = []
	with open(filename, "r") as f:
		for line in tqdm([ln.rstrip('\n') for ln in f.readlines()]):
			i = 0
			x = y = z = 0
			while i < len(line):
				if line[i] == "s":
					z += 1
					i += 1
					if line[i] == "e":
						y -= 1
					elif line[i] == "w":
						x -= 1
				elif line[i] == "n":
					z -= 1
					i += 1
					if line[i] == "e":
						x += 1
					elif line[i] == "w":
						y += 1
				elif line[i] == "e":
					x += 1
					y -= 1
				elif line[i] == "w":
					x -= 1
					y += 1
				i += 1
			# print(x, y, z)
			for tile in tiles:
				if tile.position == (x, y, z):
					tile.flip()
					break
			else:
				tiles.append(Tile((x, y, z), white=False))
	cnt = 0
	for tile in tiles:
		if not tile.white:
			cnt += 1
	print("Part 1: ", cnt)
	return tiles
			
def tuple_sum(tup1, tup2):
	return tuple([tup1[i] + tup2[i] for i in range(len(tup1))])
			
def part_2():
	tiles = blist(part_1())
	for day in tqdm(range(1,101)):
		tiles_to_check = blist([])
		# print([(tl.position, tl.white) for tl in tiles])
		for tile in tiles:
			tiles_to_check.append(Tile(tile.position, tile.white))
		# print([(tl.position, tl.white) for tl in tiles_to_check])
		for tile in tiles:
			if not tile.white:
				for op in [(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)]:
					new_pos = tuple_sum(tile.position, op)
					for tile2 in tiles_to_check:
						if tile2.position == new_pos:
							break
					else:
						tiles_to_check.append(Tile(new_pos))
		# print([(tl.position, tl.white) for tl in tiles_to_check])
		for tile in tiles_to_check:
			cont = 0
			# print("Checking tile ", tile.position, tile.white)
			for op in [(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)]:
				new_pos = tuple_sum(tile.position, op)
				# print("new pos", new_pos)
				for tile2 in tiles:
					# print(tile2.position, new_pos, tile2.position == new_pos)
					if tile2.position == new_pos:
						if not tile2.white:
							# print(tile2.position, "is black and adjacent")
							cont += 1
						break
			if tile.white and cont == 2:
				# print("Flipping white")
				tile.flip()
			if not tile.white and (cont == 0 or cont > 2):
				# print("Flipping black")
				tile.flip()
		tiles = tiles_to_check
		for tile in tiles:
			if tile.white:
				tiles.remove(tile)
	cnt = 0
	for tile in tiles:
		if not tile.white:
			cnt += 1
	print("Part 2: ", cnt)
	
part_2()
				
