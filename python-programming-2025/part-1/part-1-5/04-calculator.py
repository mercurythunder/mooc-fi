n = int(input("Number 1: "))
m = int(input("Number 2: "))
op = input("Operation: ")
if op == "add":
	print(f"{n} + {m} = {n + m}")
if op == "subtract":
	print(f"{n} - {m} = {n - m}")
if op == "multiply":
	print(f"{n} * {m} = {n * m}")