class SimpleDate:
	def __init__(self, day: int, month: int, year: int):
		self.__day = day
		self.__month = month
		self.__year = year
	
	@property
	def day(self):
		return self.__day
	
	@property
	def month(self):
		return self.__month
	
	@property
	def year(self):
		return self.__year
	
	def __str__(self):
		return f"{self.day}.{self.month}.{self.year}"

	def __gt__(self, another):
		return (self.year > another.year) or (self.year == another.year and self.month > another.month) or (self.year == another.year and self.month == another.month and self.day > another.day)
	
	def __lt__(self, another):
		return (self.year < another.year) or (self.year == another.year and self.month < another.month) or (self.year == another.year and self.month == another.month and self.day < another.day)
	
	def __eq__(self, another):
		return self.year == another.year and self.month == another.month and self.day == another.day
	
	def __ne__(self, another):
		return self.year != another.year or self.month != another.month or self.day != another.day
	
	def __add__(self, days: int):
		days_added = days % 30
		months_added = days // 30
		years_added = days // 360
		months_added = months_added - (years_added * 12)
		new_day = self.day + days_added
		new_month = self.month + months_added
		new_year = self.year + years_added
		if self.day + days_added > 30:
			new_day -= 30
			new_month += 1
		if self.month + months_added > 12:
			new_month -= 12
			new_year += 1
		return SimpleDate(new_day, new_month, new_year)

	def __sub__(self, another):
		if self.year == another.year and self.month == another.month:
			return abs(self.day - another.day)
		elif self.year == another.year:
			return abs((self.month - another.month) * 30 + (self.day - another.day))
		else:
			return abs(((self.year - another.year) * 360) + ((self.month - another.month) * 30) + (self.day - another.day))

if __name__ == "__main__":
	# Test 1
	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(28, 12, 1985)
	d3 = SimpleDate(28, 12, 1985)
	print(d1)
	print(d2)
	print(d1 == d2)
	print(d1 != d2)
	print(d1 == d3)
	print(d1 < d2)
	print(d1 > d2)
	# Test 2
	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(28, 12, 1985)
	d3 = d1 + 3
	d4 = d2 + 400
	print(d1)
	print(d2)
	print(d3)
	print(d4)
	# Test 3
	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(2, 11, 2020)
	d3 = SimpleDate(28, 12, 1985)
	print(d2-d1)
	print(d1-d2)
	print(d1-d3)