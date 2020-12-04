import re

filename = "input.txt"

mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part_1():
	valid_passports = 0
	with open(filename, "r") as f:
		found_keys = []
		for line in f.readlines():
			if line == '\n':
				if len(found_keys) == 8:
					valid_passports += 1
				elif len(found_keys) == 7:
					if "cid" not in found_keys:
						valid_passports += 1
				found_keys = []
			else:
				for pair in line.split(" "):
					found_keys.append(pair.split(":")[0])
							
	print("Part 1: ", valid_passports)
	
def part_2():
	valid_passports = 0
	with open(filename, "r") as f:
		found_keys = []
		for line in f.readlines():
			if line == '\n':
				if len(found_keys) == 8:
					valid_passports += 1
				elif len(found_keys) == 7:
					if "cid" not in found_keys:
						valid_passports += 1
				found_keys = []
			else:
				print(line)
				for pair in line[:-1].split(" "):
					key, value = pair.split(":")
					if key == "byr":
						if int(value) >= 1920 and int(value) <= 2002:
							found_keys.append(key)
					elif key == "iyr":
						if int(value) >= 2010 and int(value) <= 2020:
							found_keys.append(key)
					elif key == "eyr":
						if int(value) >= 2020 and int(value) <= 2030:
							found_keys.append(key)
					elif key == "hgt":
						print("Altura", value, value[-2:], value[:-2])
						if value[-2:] == "in":
							if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
								print("added")
								found_keys.append(key)
						elif value[-2:] == "cm":
							if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
								print("added")
								found_keys.append(key)
					elif key == "hcl":
						if re.match("#[a-f0-9]{6}",value):
							found_keys.append(key)
					elif key == "ecl":
						if value in ["amb","blu","brn","gry","grn","hzl","oth"]:
							found_keys.append(key)
					elif key == "pid":
						if len(value) == 9:
							try:
								val = int(value)
								found_keys.append(key)
							except ValueError:
								pass
					elif key == "cid":
						found_keys.append(key)
							
	print("Part 2: ", valid_passports)
			
part_2()
			
