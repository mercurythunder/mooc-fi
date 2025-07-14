def transpose(matrix: list):
	x = len(matrix)
	y = len(matrix[0])
	for i in range(x):
		for j in range(i + 1, y):
			swap = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = swap