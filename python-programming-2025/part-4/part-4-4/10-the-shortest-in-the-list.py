def shortest(mylist):
	theshortest = ""
	for string in mylist:
		if theshortest == "" or len(theshortest) > len(string):
			theshortest = string
	return theshortest

if __name__ == "__main__":
	my_list = ["first", "second", "fourth", "eleventh"]
	result = shortest(my_list)
	print(result)