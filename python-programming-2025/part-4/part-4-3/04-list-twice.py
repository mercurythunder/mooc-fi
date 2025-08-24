mylist = []
while True:
	item = int(input("New item: "))
	if item == 0:
		break
	mylist.append(item)
	print(f"The list now: {mylist}")
	print(f"The list in order: {sorted(mylist)}")
print("Bye!")