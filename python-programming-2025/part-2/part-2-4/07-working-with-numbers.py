numbers = list()

print("Please type in integer numbers. Type in 0 to finish.")
number = int(input("Number: "))
while number != 0:
	numbers.append(number)
	number = int(input("Number: "))

print(f"Numbers typed in {len(numbers)}")

total = 0
positives = 0
for number in numbers:
	total += number
	if number >= 0:
		positives += 1
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / len(numbers)}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {len(numbers) - positives}")