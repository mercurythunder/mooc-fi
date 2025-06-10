string = input("Please type in a word: ")
to_find = input("Please type in a character: ")

while string != "":
	start = string.find(to_find)
	if start >= 0 and start <= (len(string) - 3):
		print(string[start:(start + 3)])
		string = string[(start + 1):]
	else:
		break