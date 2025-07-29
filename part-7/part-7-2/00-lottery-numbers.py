from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
	pool = list(range(lower, upper))
	draw = sample(pool, amount)
	draw.sort()
	return draw

if __name__ == "__main__":
	for number in lottery_numbers(7, 1, 40):
		print(number)