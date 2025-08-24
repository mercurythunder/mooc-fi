number = int(input("Please type in a number: "))
i = 1000
while i > number and i >= 10:
	print(f"This number is smaller than {int(i)}")
	i = i / 10
print("Thank you!")