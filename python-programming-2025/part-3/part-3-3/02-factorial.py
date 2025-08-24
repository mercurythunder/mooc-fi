number = int(input("Please type in a number: "))
factorial = 1

while number > 0:
	for i in range (1, number + 1):
		factorial *= i
	print(f"The factorial of the number {number} is {factorial}")
	factorial = 1
	number = int(input("Please type in a number: "))

print("Thanks and bye!")