filename = "input.txt"

def part_1():
	with open(filename, "r") as f:
		departing_time = int(f.readline().rstrip('\n'))
		buses = []
		for elem in f.readline().rstrip('\n').split(','):
			try:
				time = int(elem)
			except ValueError:
				continue
			buses.append(time)
	min_waiting = None
	min_bus = None
	for bus in buses:
		if departing_time % bus == 0:
			print("Minim bus: ", bus)
			min_waiting = 0
			min_bus = bus
		else:
			waiting_time = (bus * ((departing_time // bus) + 1)) - departing_time
			if min_waiting is None or waiting_time < min_waiting:
				print("Minim bus i temps: ", bus, waiting_time)
				min_waiting = waiting_time
				min_bus = bus
	print("Part 1: ", min_bus * min_waiting)
	
def part_2():
	with open(filename, "r") as f:
		departing_time = int(f.readline().rstrip('\n'))
		buses = []
		offsets = []
		i = 0
		for elem in f.readline().rstrip('\n').split(','):
			try:
				time = int(elem)
				buses.append(time)
				offsets.append(i)
			except ValueError:
				pass
			i += 1
	print(buses, offsets)
	lp = 0
	while True:
		# print(t)
		isDivisible = True
		for i in range(5):
			if i == 0:
				continue
			if (lp + offsets[i]) % buses[i] != 0:
				isDivisible = False
				break
		if isDivisible:
			loop_point = lp
			break
		lp += buses[0]
	print(loop_point)
	t = loop_point
	mcm = buses[0] * buses[1] * buses[2] * buses[3] * buses[4]
	while True:
		print(t)
		isDivisible = True
		for i in range(5, len(buses)):
			if i == 0:
				continue
			if (t + offsets[i]) % buses[i] != 0:
				isDivisible = False
				break
		if isDivisible:
			print("Part 2: ", t)
			break
		t += mcm
			
part_2()
