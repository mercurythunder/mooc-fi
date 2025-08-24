def double_items(numbers: list):
	output = list()
	for number in numbers:
		output.append(number * 2)
	return output

if __name__ == "__main__":
	numbers = [2, 4, 5, 3, 11, -4]
	numbers_doubled = double_items(numbers)
	print("original:", numbers)
	print("doubled:", numbers_doubled)