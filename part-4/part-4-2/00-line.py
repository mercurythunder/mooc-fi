def line(length, character):
	if character == "":
		print("*" * length)
	else:
		print(character[0] * length)

if __name__ == "__main__":
	line(5, "x")