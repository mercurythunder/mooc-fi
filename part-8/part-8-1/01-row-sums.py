def row_sums(my_matrix: list):
	rows = len(my_matrix)
	columns = len(my_matrix[0])
	row_sum = 0
	for i in range(0, rows):
		for j in range(0, columns):
			row_sum += my_matrix[i][j]
		my_matrix[i].append(row_sum)
		row_sum = 0

if __name__ == "__main__":
	my_matrix = [[1, 2], [3, 4]]
	row_sums(my_matrix)
	print(my_matrix)