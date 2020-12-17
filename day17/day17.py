import numpy as np
from copy import deepcopy
import itertools

filename = "input.txt"

class Cube:
	def __init__(self, original_list):
		self.data = np.array(original_list)
		
	def _capa_buida(self, new_files, new_elems):
		return [[0] * new_elems for _ in range(new_files)]
		
	def needs_expansion(self):
		# Mirar la 1a i última capa i les primeres i últimes files i columnes de cada capa
		# Capes
		if self.data.ndim > 2:
			if self.data[0].sum() > 0 or self.data[-1].sum() > 0:
				return True
		# Files 
		if self.data[:,0,].sum() > 0 or self.data[:,-1,].sum() > 0:
			return True
		# Columnes
		if self.data[:,:,0].sum() > 0 or self.data[:,:,-1].sum() > 0:
			return True
		return False
	
	def adjacents(self, c_capa, c_line, c_elem):
		possible_capes = []
		possible_lines = []
		possible_cols = []
		for sumador in [-1,0,1]:
			if c_capa + sumador >= 0 and c_capa + sumador < len(self.data):
				possible_capes.append(c_capa + sumador)
			if c_line + sumador >= 0 and c_line + sumador < len(self.data[c_capa]):
				possible_lines.append(c_line + sumador)
			if c_elem + sumador >= 0 and c_elem + sumador < len(self.data[c_capa][c_line]):
				possible_cols.append(c_elem + sumador)
		perms = []
		for p in itertools.product(possible_capes, possible_lines, possible_cols):
			if p[0] == c_capa and p[1] == c_line and p[2] == c_elem:
				continue
			perms.append(p)
		return perms
	
	def update(self):
		new_cube = deepcopy(self.data)
		for c_capa, capa in enumerate(self.data):
			for c_line, line in enumerate(capa):
				for c_elem, elem in enumerate(line):
					adj_actives = 0
					# print("Elem at ", c_capa, c_line, c_elem)
					for adj in self.adjacents(c_capa, c_line, c_elem):
						# print("ADJ: ",adj[0], adj[1], adj[2]) 
						if self.data[adj[0]][adj[1]][adj[2]] == 1:
							adj_actives += 1
					# print("Elem at ", c_capa, c_line, c_elem, " has ", adj_actives, " actives.")
					if elem == 1:
						if adj_actives == 2 or adj_actives == 3:
							new_cube[c_capa][c_line][c_elem] = 1
						else:
							new_cube[c_capa][c_line][c_elem] = 0
					else:
						if adj_actives == 3:
							new_cube[c_capa][c_line][c_elem] = 1
						else:
							new_cube[c_capa][c_line][c_elem] = 0
		self.data = new_cube		
	
	def expand(self):
		try:
			num_capes, num_files, num_elems = self.data.shape
		except ValueError:
			num_capes = 1
			num_files, num_elems = self.data.shape
		new_capes = num_capes + 2 # Nova capa al davant i al darrere
		new_files = num_files + 2 # A dalt i a baix
		new_elems = num_elems + 2 # Al principi i al final
		new_cube = []
		for c_capa in range(new_capes):
			if c_capa == 0 or c_capa == new_capes - 1:
				new_cube.append(self._capa_buida(new_files, new_elems))
			else:
				new_capa = []
				for c_fila in range(new_files):
					if c_fila == 0 or c_fila == new_files - 1:
						new_capa.append([0] * new_elems)
					else:
						new_fila = [0]
						if new_capes > 3:
							for n in self.data[c_capa - 1][c_fila - 1]:
								new_fila.append(n)
						else:
							for n in self.data[c_fila - 1]:
								new_fila.append(n)
						new_fila.append(0)
						new_capa.append(new_fila)
				new_cube.append(new_capa)
		self.data = np.array(new_cube)
		
def read_input():
	inp = []
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			inp.append([1 if c == '#' else 0 for c in line])
	return inp
			
		
def part_1():
	cube = Cube(read_input())
	cube.expand()
	print(cube.data)
	for t in range(6):
		cube.update()
		if cube.needs_expansion():
			cube.expand()
	print(cube.data)
	print("Part 1: ", cube.data.sum())
	
class Cube2:
	def __init__(self, original_list):
		self.data = np.array(original_list)
		
	def _capa_buida(self, new_files, new_elems):
		return [[0] * new_elems for _ in range(new_files)]
		
	def needs_expansion(self):
		# Mirar la 1a i última capa i les primeres i últimes files i columnes de cada capa
		# Hypers
		if self.data[:,:,:,0].sum() > 0 or self.data[:,:,:,-1].sum() > 0:
			return True
		# Capes
		if self.data[0,:,].sum() > 0 or self.data[-1,:,].sum() > 0:
			return True
		# Files 
		if self.data[:,0,].sum() > 0 or self.data[:,-1,].sum() > 0:
			return True
		# Columnes
		if self.data[:,:,0].sum() > 0 or self.data[:,:,-1].sum() > 0:
			return True
		return False
	
	def adjacents(self, c_capa, c_line, c_elem, c_hyper):
		possible_capes = []
		possible_lines = []
		possible_cols = []
		possible_hypers = []
		for sumador in [-1,0,1]:
			if c_capa + sumador >= 0 and c_capa + sumador < len(self.data):
				possible_capes.append(c_capa + sumador)
			if c_line + sumador >= 0 and c_line + sumador < len(self.data[c_capa]):
				possible_lines.append(c_line + sumador)
			if c_elem + sumador >= 0 and c_elem + sumador < len(self.data[c_capa][c_line]):
				possible_cols.append(c_elem + sumador)
			if c_hyper + sumador >= 0 and c_hyper + sumador < len(self.data[c_capa][c_line][c_elem]):
				possible_hypers.append(c_hyper + sumador)
		perms = []
		for p in itertools.product(possible_capes, possible_lines, possible_cols, possible_hypers):
			if p[0] == c_capa and p[1] == c_line and p[2] == c_elem and p[3] == c_hyper:
				continue
			perms.append(p)
		return perms
	
	def update(self):
		new_cube = deepcopy(self.data)
		for c_capa, capa in enumerate(self.data):
			for c_line, line in enumerate(capa):
				for c_elem, elem in enumerate(line):
					for c_hyper, hyper in enumerate(elem):
						adj_actives = 0
						# print("Elem at ", c_capa, c_line, c_elem)
						for adj in self.adjacents(c_capa, c_line, c_elem, c_hyper):
							# print("ADJ: ",adj[0], adj[1], adj[2]) 
							if self.data[adj[0]][adj[1]][adj[2]][adj[3]] == 1:
								adj_actives += 1
						# print("Elem at ", c_capa, c_line, c_elem, " has ", adj_actives, " actives.")
						if hyper == 1:
							if adj_actives == 2 or adj_actives == 3:
								new_cube[c_capa][c_line][c_elem][c_hyper] = 1
							else:
								new_cube[c_capa][c_line][c_elem][c_hyper] = 0
						else:
							if adj_actives == 3:
								new_cube[c_capa][c_line][c_elem][c_hyper] = 1
							else:
								new_cube[c_capa][c_line][c_elem][c_hyper] = 0
		self.data = new_cube		
	
	def expand(self):
		try:
			num_capes, num_files, num_elems, num_hypers = self.data.shape
		except ValueError:
			num_capes = 1
			try:
				num_files, num_elems, num_hypers = self.data.shape
			except ValueError:
				num_files = 1
				num_elems, num_hypers = self.data.shape
		new_capes = num_capes + 2 # Nova capa al davant i al darrere
		new_files = num_files + 2 # A dalt i a baix
		new_elems = num_elems + 2 # Al principi i al final
		new_hypers = num_hypers + 2
		new_cube = []
		if num_files == 1:
			print(self.data.shape)
			print(self.data)
			for f in range(new_files):
				new_fila = [[0] * len(self.data[f])]
				for e in range(new_elems):
					new_elem = [0]
					for h in range(new_hypers):
						new_elem.append(h)
					new_elem.append(0)
					new_fila.append(new_elem)
				new_fila.append([0] * len(self.data[f]))
				new_cube.append(new_fila)
		else:
			for c in range(new_capes):
				new_capa = [[[0] * len(self.data[c][0])] * len(self.data[c])]
				for f in range(new_files):
					new_fila = [[0] * len(self.data[c][f][0])]
					for e in range(new_elems):
						new_elem = [0]
						for h in range(new_hypers):
							new_elem.append(h)
						new_elem.append(0)
						new_fila.append(new_elem)
					new_fila.append([0] * len(self.data[c][f][0]))
					new_capa.append(new_fila)
				new_capa.append([[[0] * len(self.data[c][0])] * len(self.data[c])])
				new_cube.append(new_capa)
		self.data = np.array(new_cube)
		
def part_2():
	cube = Cube2(read_input())
	cube.expand()
	print(cube.data)
	for t in range(6):
		cube.update()
		if cube.needs_expansion():
			cube.expand()
	print(cube.data)
	print("Part 2: ", cube.data.sum())


part_2()
