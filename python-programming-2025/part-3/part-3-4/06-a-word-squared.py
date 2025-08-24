def squared(string, size):
	length = len(string)
	index = 0
	result = ""
	for i in range (0, size):
		for j in range (0, size):
			result += string[index]
			index += 1
			if index >= length:
				index = 0
		result += "\n"
	print(result)

if __name__ == "__main__":
	squared("capybara", 7)