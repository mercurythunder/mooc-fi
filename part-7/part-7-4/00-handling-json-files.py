from json import *

def print_persons(filename: str):
	file = open(filename)
	students = loads(file.read())
	string = ""
	for student in students:
		string += student["name"]
		string += " "
		string += str(student["age"])
		string += " years ("
		hobbies = student["hobbies"]
		for hobby in hobbies:
			string += hobby
			string += ", "
		if len(hobbies) > 0:
			string = string[:-2]
		string += ")\n"
	print(string)

if __name__ == "__main__":
	print_persons("file1.json")
	print_persons("file2.json")
	print_persons("file3.json")
	print_persons("file4.json")