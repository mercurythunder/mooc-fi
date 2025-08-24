import sys

def largest():
	filename = "numbers.txt"
	largest = - (sys.maxsize * 2)
	with open(filename) as file:
		for line in file:
			number = int(line)
			if number > largest:
				largest = number
	return largest

if __name__ == "__main__":
	print(largest())