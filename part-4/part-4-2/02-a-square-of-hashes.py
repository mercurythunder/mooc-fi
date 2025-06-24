def line(length, character):
	if character == "":
		print("*" * length)
	else:
		print(character[0] * length)

def square_of_hashes(size):
	for i in range (0, size):
		line(size, "#")

if __name__ == "__main__":
	square_of_hashes(5)