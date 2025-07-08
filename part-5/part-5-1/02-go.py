def who_won(game_board: list):
	ones = 0
	twos = 0
	for row in game_board:
		for square in row:
			if square == 1:
				ones += 1
			elif square == 2:
				twos += 1
	if ones > twos:
		return 1
	elif ones < twos:
		return 2
	else:
		return 0