def store_personal_data(person: tuple):
	filename = "people.csv"
	add_person = ""
	with open(filename, "a") as file:
		for token in person:
			add_person += str(token)
			add_person += ";"
		add_person = add_person[:-1] # Remove the last ";"
		file.write(add_person)

if __name__ == "__main__":
	person = ("Paul Paulson", 37, 175.5)
	store_personal_data(person)