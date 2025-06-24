def line(length, character):
	if character == "":
		print("*" * length)
	else:
		print(character[0] * length)

def triangle(size):
	for i in range(0, size + 1):
		line(i, "#")

if __name__ == "__main__":
	triangle(5)