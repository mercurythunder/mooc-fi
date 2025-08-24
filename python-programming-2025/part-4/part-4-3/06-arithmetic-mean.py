def mean(mylist):
	return sum(mylist) / len(mylist)

if __name__ == "__main__":
	my_list = [3, 6, -4]
	result = mean(my_list)
	print(result)