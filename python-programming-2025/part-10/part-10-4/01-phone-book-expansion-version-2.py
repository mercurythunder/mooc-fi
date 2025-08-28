class PhoneBook:
	def __init__(self):
		self.__persons = {}

	def add_number(self, name: str, number: str):
		new_person = Person(name)
		new_person.add_number(number)
		for person in self.__persons:
			if person.name() == new_person.name():
				person.add_number(number)
				return
		self.__persons[new_person] = new_person

	def get_entry(self, name: str):
		for person in self.__persons:
			if person.name() == name:
				numbers = person.numbers()
				address = person.address()
				return (numbers, address)
		return None

	def all_entries(self):
		return self.__persons

	# Added helper method
	def add_address(self, name: str, address: str):
		for person in self.__persons:
			if person.name() == name:
				person.add_address(address)
				return
		new_person = Person(name)
		new_person.add_address(address)
		self.__persons[new_person] = new_person

class PhoneBookApplication:
	def __init__(self):
		self.__phonebook = PhoneBook()

	def help(self):
		print("commands: ")
		print("0 exit")
		print("1 add number")
		print("2 search")
		print("3 add address")

	def add_number(self):
		name = input("name: ")
		number = input("number: ")
		self.__phonebook.add_number(name, number)
	
	def search(self):
		name = input("name: ")
		result = self.__phonebook.get_entry(name)
		if result == None:
			print("number unknown")
			print("address unknown")
			return
		numbers = result[0]
		address = result[1]
		if numbers == None or numbers == "" or len(numbers) < 1:
			print("number unknown")
		else:
			for number in numbers:
				print(number)
		if address == None or address == "":
			print("address unknown")
		else:
			print(address)
	
	# Added functionality
	def add_address(self):
		name = input("name: ")
		address = input("address: ")
		self.__phonebook.add_address(name, address)

	def execute(self):
		self.help()
		while True:
			print("")
			command = input("command: ")
			if command == "0":
				break
			elif command == "1":
				self.add_number()
			elif command == "2":
				self.search()
			elif command == "3":
				self.add_address()
			else:
				self.help()

# Added class
class Person:
	def __init__(self, name: str):
		self.__name = name
		self.__numbers = []
		self.__address = None
	
	def name(self):
		return self.__name
	
	def numbers(self):
		return self.__numbers
	
	def address(self):
		return self.__address
	
	def add_number(self, number: str):
		self.__numbers.append(number)
	
	def add_address(self, address: str):
		self.__address = address

# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# Test 1
'''
person = Person("Eric")
print(person.name())
print(person.numbers())
print(person.address())
person.add_number("040-123456")
person.add_address("Mannerheimintie 10 Helsinki")
print(person.numbers())
print(person.address())
'''
# Test 2
'''
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_entry("Eric"))
print(phonebook.get_entry("Emily"))
'''