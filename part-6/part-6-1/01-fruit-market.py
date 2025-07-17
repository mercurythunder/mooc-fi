def read_fruits():
	filename = "fruits.csv"
	dictionary = dict()
	with open(filename) as file:
		for line in file:
			line = line.replace("\n", "")
			data = line.split(";")
			dictionary[data[0]] = float(data[1])
	return dictionary

if __name__ == "__main__":
	print(read_fruits())