def matrix_sum():
	filename = "matrix.txt"
	sum = 0
	with open(filename) as file:
		for line in file:
			line = line.replace("\n", "")
			data = line.split(",")
			for number in data:
				sum += int(number)
	return sum

def matrix_max():
	filename = "matrix.txt"
	max_number = 0
	with open(filename) as file:
		for line in file:
			line = line.replace("\n", "")
			data = line.split(",")
			for number in data:
				if int(number) > max_number:
					max_number = int(number)
	return max_number

def row_sums():
	filename = "matrix.txt"
	sums = list()
	linesum = 0
	with open(filename) as file:
		for line in file:
			line = line.replace("\n", "")
			data = line.split(",")
			for number in data:
				linesum += int(number)
			sums.append(linesum)
			linesum = 0
	return sums

if __name__ == "__main__":
	print(matrix_sum())
	print(matrix_max())
	print(row_sums())