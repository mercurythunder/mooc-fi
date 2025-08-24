def range_of_list(mylist):
	return max(mylist) - min(mylist)

if __name__ == "__main__":
	my_list = [3, 6, -4]
	result = range_of_list(my_list)
	print(result)