def line(length, character):
	if character == "":
		print("*" * length)
	else:
		print(character[0] * length)

def shape(triangle_size, triangle_character, rectangle_size, rectangle_character):
	for i in range (0, triangle_size + 1):
		line(i, triangle_character)
	for j in range (0, rectangle_size):
		line(triangle_size, rectangle_character)

if __name__ == "__main__":
	shape(5, "x", 2, "o")