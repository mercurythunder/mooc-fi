string = input("Please type in a sentence: ")
tokens = string.split(" ")
for token in tokens:
	print(token[0])