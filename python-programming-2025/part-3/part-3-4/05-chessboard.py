def chessboard(size):
	string = ""
	for i in range (0, size):
		for j in range (0, size):
			if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
				string += "1"
			else:
				string += "0"
		string += "\n"
	print(string)

if __name__ == "__main__":
	chessboard(3)