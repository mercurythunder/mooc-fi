def times_ten(start_index: int, end_index: int):
	tens = dict()
	for i in range(start_index, end_index + 1):
		tens[i] = i * 10
	return tens

if __name__ == "__main__":
	mydict = times_ten(3, 6)
	print(mydict)