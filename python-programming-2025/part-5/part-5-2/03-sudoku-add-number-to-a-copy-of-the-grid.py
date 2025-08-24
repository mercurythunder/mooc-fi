def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
	horizontal = len(sudoku)
	vertical = len(sudoku[0])
	newsudoku = [row[:] for row in sudoku]
	for i in range(0, horizontal):
		for j in range(0, vertical):
			newsudoku[i][j] = sudoku[i][j]
			if i == row_no and j == column_no:
				newsudoku[row_no][column_no] = number
	return newsudoku

def print_sudoku(sudoku: list):
	printable = ""
	horizontal = len(sudoku)
	vertical = len(sudoku[0])
	for i in range(0, horizontal):
		for j in range(0, vertical):
			if sudoku[i][j] == 0:
				printable += "_"
			else:
				printable += str(sudoku[i][j])
			if j == (vertical - 1):
				printable += "\n"
				if (i + 1) % 3 == 0 and i != (horizontal - 1):
					printable += "\n"
			elif (j + 1) % 3 == 0:
				printable += "  "
			else:
				printable += " "
	print(printable)

if __name__ == "__main__":
	sudoku  = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]

	grid_copy = copy_and_add(sudoku, 0, 0, 2)
	print("Original:")
	print_sudoku(sudoku)
	print()
	print("Copy:")
	print_sudoku(grid_copy)