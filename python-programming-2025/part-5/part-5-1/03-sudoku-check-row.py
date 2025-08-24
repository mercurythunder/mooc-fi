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

if __name__ == "__main__":
	sudoku = [
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
	print(row_correct(sudoku, 0))
	print(row_correct(sudoku, 1))