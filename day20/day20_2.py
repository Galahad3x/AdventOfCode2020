import numpy as np
from math import sqrt
from functools import reduce

filename = "input_facil.txt"


class Tile:
	def __init__(self, tile_id, data):
		self.tile_id = tile_id
		self.data = data
		self.used = False

	def rotate_right(self):
		new_data = np.zeros(self.data.shape, dtype=np.int64)  # Les tiles son quadrades
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				new_data[j][len(self.data) - 1 - i] = self.data[i][j]
		self.data = new_data

	def flip_horizontal(self):
		new_data = np.zeros(self.data.shape, dtype=np.int64)
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				new_data[i][len(self.data) - 1 - j] = self.data[i][j]
		self.data = new_data

	def flip_vertical(self):
		new_data = np.zeros(self.data.shape, dtype=np.int64)
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				new_data[len(self.data) - 1 - i][j] = self.data[i][j]
		self.data = new_data


class Image:
	def __init__(self, num_of_tiles):
		self.size = int(sqrt(num_of_tiles))
		self.tile_array = []
		for _ in range(self.size):
			self.tile_array.append([None] * self.size)

	def print(self):
		print("\n"*20)
		for line in self.tile_array:
			st = ""
			for t in line:
				if t is not None:
					st += str(t.data)
					st += "     "
			print(st)

	def set(self, tile, position):
		pos_i, pos_j = position
		self.tile_array[pos_i][pos_j] = tile

	def unset(self, position):
		pos_i, pos_j = position
		self.tile_array[pos_i][pos_j] = None

	def corners(self):
		return [self.tile_array[0][0], self.tile_array[0][self.size - 1], self.tile_array[self.size - 1][0],
		        self.tile_array[self.size - 1][self.size - 1]]

	def fits(self, tile, position):
		pos_i, pos_j = position
		if pos_i == 0:  # No mirar a dalt
			if pos_j != 0:  # Cantonada dalt-esquerra
				if not self.fits_left(tile, position):
					return False
			if pos_j != self.size - 1:
				if not self.fits_right(tile, position):
					return False
			if not self.fits_below(tile, position):
				return False
			return True
		elif pos_i == self.size - 1:
			if pos_j != 0:  # Cantonada baix-esquerra
				if not self.fits_left(tile, position):
					return False
			if pos_j != self.size - 1:
				if not self.fits_right(tile, position):
					return False
			if not self.fits_above(tile, position):
				return False
			return True
		if pos_j != 0:  # Cantonada baix-esquerra
			if not self.fits_left(tile, position):
				return False
		if pos_j != self.size - 1:
			if not self.fits_right(tile, position):
				return False
		if not self.fits_above(tile, position):
			return False
		if not self.fits_below(tile, position):
			return False
		return True

	def fits_right(self, tile, position):  # Mirar si encaixa amb la de la dreta
		pos_i, pos_j = position
		if self.tile_array[pos_i][pos_j + 1] is None:
			return True
		else:
			return np.array_equal(tile.data[:, -1], self.tile_array[pos_i][pos_j + 1].data[:, 0])

	def fits_left(self, tile, position):  # Mirar si encaixa amb la de l'esquerra
		pos_i, pos_j = position
		if self.tile_array[pos_i][pos_j - 1] is None:
			return True
		else:
			return np.array_equal(tile.data[:, 0], self.tile_array[pos_i][pos_j - 1].data[:, -1])

	def fits_above(self, tile, position):  # Mirar si encaixa amb la de dalt
		pos_i, pos_j = position
		if self.tile_array[pos_i - 1][pos_j] is None:
			return True
		else:
			return np.array_equal(tile.data[0], self.tile_array[pos_i - 1][pos_j].data[-1])

	def fits_below(self, tile, position):  # Mirar si encaixa amb la de sota
		pos_i, pos_j = position
		if self.tile_array[pos_i + 1][pos_j] is None:
			return True
		else:
			return np.array_equal(tile.data[-1], self.tile_array[pos_i + 1][pos_j].data[0])


class Test:
	def __init__(self):
		pass

	def run_all_tests(self):
		self.rotate_right_test()
		self.flip_horizontal_test()
		self.flip_vertical_test()
		self.correct_fits_test()

	def assertEquals(self, object1, object2):
		if np.array_equal(object1, object2):
			return True
		else:
			raise ValueError

	def assertTrue(self, boolean_expression):
		if boolean_expression:
			return True
		else:
			return ValueError

	def assertFalse(self, boolean_expression):
		if not boolean_expression:
			return True
		else:
			return ValueError

	def rotate_right_test(self):
		array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
		expected = np.array([[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
		tile = Tile(1, array)
		tile.rotate_right()
		self.assertEquals(tile.data, expected)

	def flip_horizontal_test(self):
		array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
		expected = np.array([[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]])
		tile = Tile(1, array)
		tile.flip_horizontal()
		self.assertEquals(tile.data, expected)

	def flip_vertical_test(self):
		array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
		expected = np.array([[13, 14, 15, 16], [9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]])
		tile = Tile(1, array)
		tile.flip_vertical()
		self.assertEquals(tile.data, expected)

	def correct_fits_test(self):
		img = Image(9)  # 3x3
		tiles = [Tile(1, np.zeros((3, 3), dtype=np.int64))] * 9  # Tiles de tot 0s per a que encaixin si o si
		img.set(tiles[0], (0, 0))
		self.assertTrue(img.fits(tiles[1], (0, 1)))
		tiles[2].data[0][0] = 1
		self.assertFalse(img.fits(tiles[2], (1, 0)))


def _find_correct_ordering(tiles_left, current_img):
	current_img.print()
	position = None
	for i in range(current_img.size):
		for j in range(current_img.size):
			if current_img.tile_array[i][j] is None:
				position = i, j
				break
		if position is not None:
			break
	if position is None:  # Està ple
		return current_img
	# Position -> primera posició buida
	# print("Looking for position ", position)
	for tile in [t for t in tiles_left if not t.used]:
		# print("Trying tile", tile.tile_id)
		for _ in range(2):
			for _ in range(4):
				if current_img.fits(tile, position):
					# print("Tile fits ", position)
					# Eliminar tile de tiles_left, ficarlo a current_img i fer una altra volta
					tile.used = True
					current_img.set(tile, position)
					new_img = _find_correct_ordering(tiles_left, current_img)
					if new_img:
						# print("Tile found")
						return new_img
					else:
						tile.used = False
						current_img.unset(position)
				else:
					tile.rotate_right()
			tile.flip_horizontal()
	# print("No suitable tile found")
	return False


def find_correct_ordering(tiles):
	empty_img = Image(len(tiles))
	return _find_correct_ordering(tiles, empty_img)


def read_input():
	tiles = []
	with open(filename, "r") as f:
		lines = [ln.rstrip('\n') for ln in f.readlines()]
		line_c = 0
		while line_c < len(lines):
			tile_id = int(lines[line_c].split(" ")[1].rstrip(":"))
			line_c += 1
			tile_data = []
			for _ in range(10):
				tile_data.append([1 if c == "#" else 0 for c in lines[line_c]])
				line_c += 1
			line_c += 1
			tiles.append(Tile(tile_id, np.array(tile_data)))
	return tiles


def part_1():
	tiles = read_input()
	img = find_correct_ordering(tiles)
	print("Part 1: ", reduce((lambda x, y: x * y), [c.tile_id for c in img.corners()]))


part_1()
