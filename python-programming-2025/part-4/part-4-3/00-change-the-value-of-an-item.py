mylist = [1, 2, 3, 4, 5]
while True:
	index = int(input("Index: "))
	if (index < 0):
		break
	value = int(input("New value: "))
	mylist[index] = value
	print(mylist)