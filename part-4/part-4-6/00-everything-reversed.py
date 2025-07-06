def everything_reversed(mylist):
	reverselist = list()
	length = len(mylist)
	for i in range(length - 1, -1, -1):
		string = mylist[i]
		reverselist.append(string[::-1])
		length = len(mylist)
	return reverselist

if __name__ == "__main__":
	my_list = ["Hi", "there", "example", "one more"]
	new_list = everything_reversed(my_list)
	print(new_list)