def length_of_longest(mylist):
	length = 0
	for string in mylist:
		if len(string) > length:
			length = len(string)
	return length

if __name__ == "__main__":
	my_list = ["first", "second", "fourth", "eleventh"]
	result = length_of_longest(my_list)
	print(result)