def even_numbers(mylist):
	parsed = list()
	for n in mylist:
		if n % 2 == 0:
			parsed.append(n)
	return parsed

if __name__ == "__main__":
	my_list = [1, 2, 3, 4, 5]
	new_list = even_numbers(my_list)
	print("original", my_list)
	print("new", new_list)