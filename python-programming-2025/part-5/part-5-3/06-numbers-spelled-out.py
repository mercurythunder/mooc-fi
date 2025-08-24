def dict_of_numbers():
	numbers = dict()
	numbers[0] = "zero"
	for number in range(1, 100):
		if number >= 10 and number < 20:
			if number == 10:
				numbers[number] = "ten"
			elif number == 11:
				numbers[number] = "eleven"
			elif number == 12:
				numbers[number] = "twelve"
			elif number == 13:
				numbers[number] = "thirteen"
			elif number == 14:
				numbers[number] = "fourteen"
			elif number == 15:
				numbers[number] = "fifteen"
			elif number == 16:
				numbers[number] = "sixteen"
			elif number == 17:
				numbers[number] = "seventeen"
			elif number == 18:
				numbers[number] = "eighteen"
			elif number == 19:
				numbers[number] = "nineteen"
		else:
			tens = number // 10
			unit = number % 10
			numbers[number] = units(tens, unit)
	return numbers

def units(tens: int, unit: int):
	string = ""
	if tens >= 2:
		if tens == 2:
			string += "twenty"
		elif tens == 3:
			string += "thirty"
		elif tens == 4:
			string += "forty"
		elif tens == 5:
			string += "fifty"
		elif tens == 6:
			string += "sixty"
		elif tens == 7:
			string += "seventy"
		elif tens == 8:
			string += "eighty"
		elif tens == 9:
			string += "ninety"
	if tens >= 2 and unit > 0:
		string += "-"
	if unit == 1:
		string += "one"
	elif unit == 2:
		string += "two"
	elif unit == 3:
		string += "three"
	elif unit == 4:
		string += "four"
	elif unit == 5:
		string += "five"
	elif unit == 6:
		string += "six"
	elif unit == 7:
		string += "seven"
	elif unit == 8:
		string += "eight"
	elif unit == 9:
		string += "nine"
	return string

if __name__ == "__main__":
	print(dict_of_numbers())