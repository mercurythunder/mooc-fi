def square_of_letters(layers: int):
	size = layers * 2 - 1
	for i in range(0, size):
		for j in range(0, size):
			distance = min(min(i, size - i - 1), min(j, size - j - 1))
			print(chr(layers + 64 - distance), end="") # Converts position in alphabet to ASCII
		print()

square_of_letters(int(input()))