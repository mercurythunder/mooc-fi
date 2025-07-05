def formatted(floats):
	rounded = list()
	for number in floats:
		stringify = str('{0:.2f}'.format(number))
		rounded.append(stringify)
	return rounded

if __name__ == "__main__":
	my_list = [1.234, 0.3333, 0.11111, 3.446]
	new_list = formatted(my_list)
	print(new_list)