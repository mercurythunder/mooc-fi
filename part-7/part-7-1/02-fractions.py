from fractions import *

def fractionate(amount: int):
	fracts = list()
	for i in range(0, amount):
		fracts.append(Fraction(1, amount))
	return fracts

if __name__ == "__main__":
	for p in fractionate(3):
		print(p)
	print()
	print(fractionate(5))