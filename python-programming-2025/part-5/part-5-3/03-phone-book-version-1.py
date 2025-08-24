phonebook = dict()

def phonebook_select(option: int):
	if option == 1:
		name = input("name: ")
		print(phonebook_search(name))
	elif option == 2:
		name = input("name: ")
		number = input("number: ")
		phonebook_add(name, number)
		print("ok!")

def phonebook_search(name: str):
	if name not in phonebook:
		return "no number"
	else:
		return phonebook[name]

def phonebook_add(name: str, number: str):
	phonebook[name] = number

while True:
	command = int(input("command (1 search, 2 add, 3 quit): "))
	if command < 1 or command > 2:
		print("quitting...")
		break
	else:
		phonebook_select(command)