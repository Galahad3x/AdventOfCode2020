filename = "input.txt"

def read_input():
	inp = []
	with open(filename, "r") as f:
		for line in f.readlines():
			ln = line.rstrip('\n')
			inp.append(int(ln))
	return inp
	
def find_sums(nums, i, preamble):
	j = i - preamble
	while j < i:
		k = j + 1
		while k < i:
			if nums[j] + nums[k] == nums[i]:
				return 0
			k += 1
		j += 1
	return nums[i]
	
def part_1():
	nums = read_input()
	preamble = 25
	i = preamble
	while True:
		ret = find_sums(nums, i, preamble)
		# print(ret)
		if ret != 0:
			break
		i += 1
	print("Part 1: ", ret)
	return ret
	
	
def part_2():
	res = part_1()
	nums = read_input()
	range_len = 2
	while True:
		for i, num in enumerate(nums[:-(range_len - 1)]):
			ran = []
			for j in range(range_len):
				ran.append(nums[i+j])
			if sum(ran) == res:
				print("Part 2: ", min(ran) + max(ran))
				return 0
		range_len += 1
	
part_2()
