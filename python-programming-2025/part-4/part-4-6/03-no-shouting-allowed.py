def no_shouting(mylist):
	newlist = list()
	for string in mylist:
		if not string.isupper():
			newlist.append(string)
	return newlist

if __name__ == "__main__":
	my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
	pruned_list = no_shouting(my_list)
	print(pruned_list)