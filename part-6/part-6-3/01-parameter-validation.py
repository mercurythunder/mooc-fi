def new_person(name: str, age: int):
	if name == "":
		raise ValueError("Empty name")
	if " " not in name:
		raise ValueError("Name is less than two words")
	if len(name) > 40:
		raise ValueError("Name longer than 40 characters")
	if age < 0:
		raise ValueError("Negative age")
	if age > 150:
		raise ValueError("Age above 150")
	return (name, age)

if __name__ == "__main__":
	print(new_person("John Doe", 42))
	print(new_person("Harrison Ford", 83))
	print(new_person("Chewbacca", 130))
	print(new_person("Llanfair­pwllgwyngyll­gogery­chwyrn­drobwll­llan­tysilio­gogo­goch", 0))