def row_correct(sudoku: list, row_no: int):
	filled = list()
	correct = True
	for number in sudoku[row_no]:
		if number > 0:
			if number in filled:
				correct = False
				break
			else:
				filled.append(number)
	return correct

def column_correct(sudoku: list, column_no: int):
	filled = list()
	correct = True
	for row in sudoku:
		if row[column_no] > 0:
			if row[column_no] in filled:
				correct = False
				break
			else:
				filled.append(row[column_no])
	return correct

def block_correct(sudoku: list, row_no: int, column_no: int):
	filled = list()
	correct = True
	for i in range(row_no, row_no + 3):
		for j in range(column_no, column_no + 3):
			if sudoku[i][j] > 0:
				if sudoku[i][j] in filled:
					correct = False
					break
				else:
					filled.append(sudoku[i][j])
	return correct

def sudoku_grid_correct(sudoku: list):
	correct = True
	for i in range(0, len(sudoku)):
		correct = row_correct(sudoku, i)
		if not correct:
			return correct
		correct = column_correct(sudoku, i)
		if not correct:
			return correct
	for i in range(0, 7, 3):
		for j in range(0, 7, 3):
			correct = block_correct(sudoku, i, j)
			if not correct:
				return correct
	return correct

if __name__ == "__main__":
	sudoku1 = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]
	print(sudoku_grid_correct(sudoku1))

	sudoku2 = [
	[2, 6, 7, 8, 3, 9, 5, 0, 4],
	[9, 0, 3, 5, 1, 0, 6, 0, 0],
	[0, 5, 1, 6, 0, 0, 8, 3, 9],
	[5, 1, 9, 0, 4, 6, 3, 2, 8],
	[8, 0, 2, 1, 0, 5, 7, 0, 6],
	[6, 7, 4, 3, 2, 0, 0, 0, 5],
	[0, 0, 0, 4, 5, 7, 2, 6, 3],
	[3, 2, 0, 0, 8, 0, 0, 5, 7],
	[7, 4, 5, 0, 0, 3, 9, 0, 1]
	]
	print(sudoku_grid_correct(sudoku2))