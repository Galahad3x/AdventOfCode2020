import itertools

filename = "input.txt"

def apply_mask(number, mask):
	# Number un enter
	# mask un string de llargada 36
	bn = bin(number)[2:]
	while len(bn) < len(mask):
		bn = "0" + bn
	for i, ch in enumerate(mask):
		if ch == "X":
			continue
		else:
			bn = bn[:i] + ch + bn[i+1:]
	return int(bn, base=2)
	
def apply_mask_2(number, mask):
	# Number un enter
	# mask un string de llargada 36
	bn = bin(number)[2:]
	while len(bn) < len(mask):
		bn = "0" + bn
	print(bn)
	for i, ch in enumerate(mask):
		if ch == "0":
			continue
		else:
			bn = bn[:i] + ch + bn[i+1:]
	print(bn)
	addrs = []
	for prod in itertools.product("01", repeat=bn.count("X")):
		addr = bn
		p_idx = 0
		for i, ch in enumerate(addr):
			if ch == "X":
				addr = addr[:i] + prod[p_idx] + addr[i+1:]
				p_idx += 1
		addrs.append(int(addr, base=2))
	return addrs
		

def part_1():
	mask = "X" * 36
	values = {}
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			if line[1] == "a":
				mask = line.split(" ")[2]
				print("New mask: ", mask)
			elif line[1] == "e":
				spl = [st.strip(" ") for st in line.split(" = ")]
				values[int(spl[0].split("[")[1].rstrip("]"))] = apply_mask(int(spl[1]), mask)
	print("Part 1: ", sum(values.values()))
	
def part_2():
	mask = "X" * 36
	values = {}
	with open(filename, "r") as f:
		for line in [ln.rstrip('\n') for ln in f.readlines()]:
			if line[1] == "a":
				mask = line.split(" ")[2]
				print("New mask: ", mask)
			elif line[1] == "e":
				spl = [st.strip(" ") for st in line.split(" = ")]
				mem_addr = int(spl[0].split("[")[1].rstrip("]"))
				value = int(spl[1])
				for addr in apply_mask_2(mem_addr, mask):
					values[addr] = value
	print("Part 2: ", sum(values.values()))

part_2()
