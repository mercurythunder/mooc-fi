while True:
	editor = input("Editor: ")
	if editor.lower() == "word" or editor.lower() == "notepad":
		print("awful")
	elif editor.lower() != "visual studio code":
		print("not good")
	else:
		break
print("an excellent choice!")