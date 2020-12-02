filename = "input.txt"

valids = 0
with open(filename,"r") as f:
	for line in f.readlines():
		if line != '\n':
			spl = line.split(" ")
			rang = [int(n) for n in spl[0].split("-")]
			letter = spl[1][:-1]
			passwd = spl[2]
			count = passwd.count(letter)
			if count >= rang[0] and count <= rang[1]:
				valids += 1
				
print("Part 1: ", valids)

valids = 0
with open(filename,"r") as f:
	for line in f.readlines():
		if line != '\n':
			spl = line.split(" ")
			positions = [int(n) for n in spl[0].split("-")]
			letter = spl[1][:-1]
			passwd = spl[2]
			counted = 0
			try:
				if bool(passwd[positions[0] - 1] == letter) ^ bool(passwd[positions[1] - 1] == letter):
					print(passwd)
					valids += 1	
			except IndexError:
				pass
			if count == 1:
				valids += 1
				
print("Part 2: ", valids)
