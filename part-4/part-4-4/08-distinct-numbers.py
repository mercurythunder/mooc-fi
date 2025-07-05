def distinct_numbers(mylist):
	trimmed = list()
	for item in mylist:
		if item not in trimmed:
			trimmed.append(item)
	trimmed.sort()
	return trimmed

if __name__ == "__main__":
	my_list = [3, 2, 2, 1, 3, 3, 1]
	print(distinct_numbers(my_list)) # [1, 2, 3]