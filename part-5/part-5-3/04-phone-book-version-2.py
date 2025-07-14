phonebook = dict()

def phonebook_select(option: int):
	if option == 1:
		name = input("name: ")
		result = phonebook_search(name)
		if result == None:
			print("no number")
		else:
			for item in result:
				print(item)
	elif option == 2:
		name = input("name: ")
		number = input("number: ")
		phonebook_add(name, number)
		print("ok!")

def phonebook_search(name: str):
	if name not in phonebook:
		return None
	else:
		return phonebook[name]

def phonebook_add(name: str, number: str):
	if name not in phonebook:
		phonebook[name] = list()
	if number not in phonebook[name]:
		phonebook[name].append(number)

while True:
	command = int(input("command (1 search, 2 add, 3 quit): "))
	if command < 1 or command > 2:
		print("quitting...")
		break
	else:
		phonebook_select(command)