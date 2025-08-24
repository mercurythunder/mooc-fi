def read_input(message: str, minimum: int, maximum: int):
	value = minimum - 1
	while True:
		try:
			value = int(input(message))
			if minimum <= value <= maximum:
				return value
		except:
			pass
		print(f"You must type in an integer between {minimum} and {maximum}")

if __name__ == "__main__":
	number = read_input("Please type in a number: ", 5, 10)
	print("You typed in:", number)