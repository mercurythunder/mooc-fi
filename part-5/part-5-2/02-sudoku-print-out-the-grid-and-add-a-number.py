# Write your solution here
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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
	sudoku[row_no][column_no] = number 

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

	print_sudoku(sudoku)
	add_number(sudoku, 0, 0, 2)
	add_number(sudoku, 1, 2, 7)
	add_number(sudoku, 5, 7, 3)
	print()
	print("Three numbers added:")
	print()
	print_sudoku(sudoku)