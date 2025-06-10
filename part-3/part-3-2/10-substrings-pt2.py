string = input("Please type in a string: ")
letters = len(string)
for i in range(1, letters):
	print(string[-i:])
print(string)