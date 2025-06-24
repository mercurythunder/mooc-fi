def line(length, character):
	if character == "":
		print("*" * length)
	else:
		print(character[0] * length)

def box_of_hashes(height):
	for i in range (0, height):
		line(10, "#")

if __name__ == "__main__":
	box_of_hashes(5)