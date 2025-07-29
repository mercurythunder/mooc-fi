from random import *

def roll(die: str):
	rolls = list()
	if die == "A":
		rolls = [3, 3, 3, 3, 3, 6]
	elif die == "B":
		rolls = [2, 2, 2, 5, 5, 5]
	elif die == "C":
		rolls = [1, 4, 4, 4, 4, 4]
	return choice(rolls)

def play(die1: str, die2: str, times: int):
	rolls1 = list()
	rolls2 = list()
	if die1 == "A":
		rolls1 = [3, 3, 3, 3, 3, 6]
	elif die1 == "B":
		rolls1 = [2, 2, 2, 5, 5, 5]
	elif die1 == "C":
		rolls1 = [1, 4, 4, 4, 4, 4]
	if die2 == "A":
		rolls2 = [3, 3, 3, 3, 3, 6]
	elif die2 == "B":
		rolls2 = [2, 2, 2, 5, 5, 5]
	elif die2 == "C":
		rolls2 = [1, 4, 4, 4, 4, 4]
	wins1 = 0
	wins2 = 0
	ties = 0
	for i in range(0, times):
		roll1 = choice(rolls1)
		roll2 = choice(rolls2)
		if roll1 > roll2:
			wins1 += 1
		elif roll1 == roll2:
			ties += 1
		else:
			wins2 += 1
	return (wins1, wins2, ties)

if __name__ == "__main__":
	for i in range(20):
		print(roll("A"), " ", end="")
	print()
	for i in range(20):
		print(roll("B"), " ", end="")
	print()
	for i in range(20):
		print(roll("C"), " ", end="")