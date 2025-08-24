class Money:
	def __init__(self, euros: int, cents: int):
		self.__euros = euros
		self.__cents = cents

	def __str__(self):
		if self.__cents < 10:
			return f"{self.__euros}.0{self.__cents} eur"
		else:
			return f"{self.__euros}.{self.__cents} eur"
	
	def __eq__(self, another):
		return (self.__euros == another.__euros) and (self.__cents == another.__cents)
	
	def __ne__(self, another):
		return not self.__eq__(another)
	
	def __gt__(self, another):
		return (self.__euros > another.__euros) or ((self.__euros == another.__euros) and (self.__cents > another.__cents))
	
	def __lt__(self, another):
		return (self.__euros < another.__euros) or ((self.__euros == another.__euros) and (self.__cents < another.__cents))
	
	def __add__(self, another):
		if self.__cents + another.__cents < 100:
			return Money(self.__euros + another.__euros, self.__cents + another.__cents)
		else:
			return Money(self.__euros + another.__euros + 1, self.__cents + another.__cents - 100)
	
	def __sub__(self, another):
		if self.__lt__(another):
			raise ValueError("A negative result is not allowed")
		if self.__cents >= another.__cents:
			return Money(self.__euros - another.__euros, self.__cents - another.__cents)
		else:
			return Money(self.__euros - another.__euros - 1, self.__cents - another.__cents + 100)

if __name__ == "__main__":
	# Test 1
	e1 = Money(4, 10)
	e2 = Money(2, 5)  # two euros and five cents
	print(e1)
	print(e2)
	# Test 2
	e1 = Money(4, 10)
	e2 = Money(2, 5)
	e3 = Money(4, 10)
	print(e1)
	print(e2)
	print(e3)
	print(e1 == e2)
	print(e1 == e3)
	# Test 3
	e1 = Money(4, 10)
	e2 = Money(2, 5)
	print(e1 != e2)
	print(e1 < e2)
	print(e1 > e2)
	# Test 4
	e1 = Money(4, 5)
	e2 = Money(2, 95)
	e3 = e1 + e2
	e4 = e1 - e2
	print(e3)
	print(e4)
	e5 = e2-e1