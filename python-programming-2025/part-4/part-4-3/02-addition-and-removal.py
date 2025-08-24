mylist = []
last_added = 0
print(f"The list is now {mylist}")
while True:
	command = input("a(d)d, (r)emove or e(x)it: ")
	if command == "x":
		break
	if command == "r":
		if len(mylist) >= 0:
			mylist.pop()
	if command == "d":
		if len(mylist) <= 0:
			mylist.append(1)
		else:
			last_added = mylist.pop()
			mylist.append(last_added)
			mylist.append(last_added + 1)
	print(f"The list is now {mylist}")
print("Bye!")