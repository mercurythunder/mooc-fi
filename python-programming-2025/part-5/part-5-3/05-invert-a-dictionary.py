def invert(dictionary: dict):
	inverted = dict()
	for key, value in dictionary.items():
		inverted[value] = key
	dictionary.clear()
	for key, value in inverted.items():
		dictionary[key] = value

if __name__ == "__main__":
	s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
	invert(s)
	print(s)