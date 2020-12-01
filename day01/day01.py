filename = "input.txt"

prices = []
with open(filename, "r") as f:
	for line in f.readlines()[:-1]:
		prices.append(int(line[:-1]))
		
print("Part 1: ")
for price in prices:
	for price2 in prices:
			if price + price2 == 2020:
				print(price * price2)
		
print("Part 2: ")
for price in prices:
	for price2 in prices:
		for price3 in prices:
			if price + price2 + price3 == 2020:
				print(price * price2 * price3)
