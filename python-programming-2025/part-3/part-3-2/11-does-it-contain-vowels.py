string = input("Please type in a string: ")
for letter in ("a", "e", "o"):
	if letter in string:
		print(f"{letter} found")
	else:
		print(f"{letter} not found")