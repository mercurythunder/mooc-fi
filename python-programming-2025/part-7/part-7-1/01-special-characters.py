from string import *

def separate_characters(my_string: str):
	letters = ""
	punct = ""
	other = ""
	for char in my_string:
		if char in ascii_letters:
			letters += char
		elif char in punctuation:
			punct += char
		else:
			other += char
	return (letters, punct, other)

if __name__ == "__main__":
	parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
	print(parts[0])
	print(parts[1])
	print(parts[2])