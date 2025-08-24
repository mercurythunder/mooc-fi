def no_vowels(mystring):
	newstring = ""
	for char in mystring:
		if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
			newstring += char
	return newstring

if __name__ == "__main__":
	 my_string = "this is an example"
	print(no_vowels(my_string))