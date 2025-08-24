class NumberStats:
	def __init__(self):
		self.numbers = 0
		self.stored_numbers = list()

	def add_number(self, number: int):
		self.numbers += 1
		self.stored_numbers.append(number)

	def count_numbers(self):
		return self.numbers

	def get_sum(self):
		sum = 0
		for number in self.stored_numbers:
			sum += number
		return sum
	
	def average(self):
		if self.numbers == 0:
			return 0
		sum = self.get_sum()
		return sum / self.numbers

stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())
stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())

stats = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()
print("Please type in integer numbers: ")
while True:
	number = int(input())
	if number == -1:
		break
	stats.add_number(number)
	if number % 2 == 0:
		stats_even.add_number(number)
	else:
		stats_odd.add_number(number)
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())