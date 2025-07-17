import sys

def largest():
	largest = - (sys.maxsize * 2)
	with open("numbers.txt") as file:
		for line in file:
			number = int(line)
			if number > largest:
				largest = number
	return largest

if __name__ == "__main__":
	print(largest())