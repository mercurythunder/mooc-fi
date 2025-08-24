def factorials(n: int):
	fact = dict()
	prev = 1
	for i in range(1, n + 1):
		fact[i] = i * prev
		prev = fact[i]
	return fact

if __name__ == "__main__":
	mydict = factorials(10)
	print(mydict)