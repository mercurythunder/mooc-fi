def spruce(cap):
	print("a spruce!")
	for i in range (1, cap + 1):
		print(" " * (cap - i) + "*" * (i * 2 - 1))
	print(" " * (cap - 1) + "*")

if __name__ == "__main__":
	spruce(5)