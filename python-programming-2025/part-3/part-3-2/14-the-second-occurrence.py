string = input("Please type in a string: ")
to_find = input("Please type in a substring: ")
first = False
printed = False
trimmed = 0

while string != "":
	start = string.find(to_find)
	if start >= 0 and start < (len(string)):
		if first:
			print(f"The second occurrence of the substring is at index {start + trimmed}.")
			printed = True
			break
		else:
			first = True
			string = string[(start + len(to_find)):]
			trimmed = start + len(to_find)
	else:
		break

if not first or not printed:
	print("The substring does not occur twice in the string.")