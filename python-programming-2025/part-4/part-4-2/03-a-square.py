def line(length, character):
	if character == "":
		print("*" * length)
	else:
		print(character[0] * length)

def square(size, character):
	for i in range (0, size):
		line(size, character)

if __name__ == "__main__":
	square(5, "x")