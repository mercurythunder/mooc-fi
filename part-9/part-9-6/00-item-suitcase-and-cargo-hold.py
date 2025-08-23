class Item:
	def __init__(self, name: str, weight: int):
		self.__name = name
		self.__weight = weight
	
	def __str__(self):
		return f"{self.__name} ({self.__weight} kg)"

	# @property # Calling name() will result in an error if this method is defined with @property
	def name(self):
		return self.__name
	
	# @property # Calling weight() will result in an error if this method is defined with @property
	def weight(self):
		return self.__weight

class Suitcase:
	def __init__(self, max_weight: int):
		self.__max_weight = max_weight
		self.__items = list()
	
	def __str__(self):
		if len(self.__items) == 1:
			return f"1 item ({self.weight()} kg)"
		return f"{len(self.__items)} items ({self.weight()} kg)"

	@property
	def max_weight(self):
		return self.__max_weight
	
	@property
	def items(self):
		return self.__items

	def weight(self):
		weight = 0
		for item in self.__items:
			weight += item.weight()
		return weight
	
	def add_item(self, item: Item):
		if self.weight() + item.weight() <= self.__max_weight:
			self.__items.append(item)
	
	def heaviest_item(self):
		if len(self.__items) == 0:
			return None
		heaviest_weight = 0
		heaviest_item = ""
		for item in self.__items:
			if item.weight() > heaviest_weight:
				heaviest_weight = item.weight()
				heaviest_item = item
		return heaviest_item

	def print_items(self):
		for item in self.__items:
			print(item)

class CargoHold:
	def __init__(self, max_weight: int):
		self.__max_weight = max_weight
		self.__suitcases = list()
	
	def __str__(self):
		if len(self.__suitcases) == 1:
			return f"1 suitcase, space for {self.__max_weight - self.weight()} kg"
		return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.weight()} kg"
	
	@property
	def max_weight(self):
		return self.__max_weight
	
	@property
	def suitcases(self):
		return self.__suitcases
	
	def weight(self):
		weight = 0
		for suitcase in self.__suitcases:
			weight += suitcase.weight()
		return weight
	
	def add_suitcase(self, suitcase: Suitcase):
		if self.weight() + suitcase.weight() <= self.__max_weight:
			self.__suitcases.append(suitcase)
	
	def print_items(self):
		for suitcase in self.__suitcases:
			for item in suitcase.items:
				print(item)

if __name__ == "__main__":
	# Test 1
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	print("Name of the book:", book.name())
	print("Weight of the book:", book.weight())
	print("Book:", book)
	print("Phone:", phone)
	book = Item("ABC Book", 2)
	# Test 2-3
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	suitcase = Suitcase(5)
	print(suitcase)
	suitcase.add_item(book)
	print(suitcase)
	suitcase.add_item(phone)
	print(suitcase)
	suitcase.add_item(brick)
	print(suitcase)
	# Test 4
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	suitcase = Suitcase(10)
	suitcase.add_item(book)
	suitcase.add_item(phone)
	suitcase.add_item(brick)
	print("The suitcase contains the following items:")
	suitcase.print_items()
	combined_weight = suitcase.weight()
	print(f"Combined weight: {combined_weight} kg")
	# Test 5
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	suitcase = Suitcase(10)
	suitcase.add_item(book)
	suitcase.add_item(phone)
	suitcase.add_item(brick)
	heaviest = suitcase.heaviest_item()
	print(f"The heaviest item: {heaviest}")
	# Test 6
	cargo_hold = CargoHold(1000)
	print(cargo_hold)
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	adas_suitcase = Suitcase(10)
	adas_suitcase.add_item(book)
	adas_suitcase.add_item(phone)
	peters_suitcase = Suitcase(10)
	peters_suitcase.add_item(brick)
	cargo_hold.add_suitcase(adas_suitcase)
	print(cargo_hold)
	cargo_hold.add_suitcase(peters_suitcase)
	print(cargo_hold)
	# Test 7
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	adas_suitcase = Suitcase(10)
	adas_suitcase.add_item(book)
	adas_suitcase.add_item(phone)
	peters_suitcase = Suitcase(10)
	peters_suitcase.add_item(brick)
	cargo_hold = CargoHold(1000)
	cargo_hold.add_suitcase(adas_suitcase)
	cargo_hold.add_suitcase(peters_suitcase)
	print("The suitcases in the cargo hold contain the following items:")
	cargo_hold.print_items()