filename = "input.txt"

inputs = []
with open(filename, "r") as f:
	for line in f.readlines():
		if line != '\n':
			inputs.append(line[:-1])
			
print("[" + ",".join(inputs) + "]")
