diary_file = "diary.txt"

def read_diary():
	print("Entries:")
	with open(diary_file) as diary:
		for line in diary:
			print(line)

def add_diary_entry(entry: str):
	with open(diary_file, "a") as diary:
		diary.write(entry + "\n")

while True:
	print("1 - add an entry, 2 - read entries, 0 - quit")
	option = int(input("Function: "))
	if option == 0:
		print("Bye now!")
		break
	elif option == 1:
		entry = input("Diary entry: ")
		add_diary_entry(entry)
		print("Diary saved")
	elif option == 2:
		read_diary()
	else:
		print("Error parsing input")
		break
