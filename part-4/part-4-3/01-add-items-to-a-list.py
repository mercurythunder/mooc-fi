mylist = []
items = int(input("How many items: "))
for i in range (1, items + 1):
	item = int(input(f"Item {i}: "))
	mylist.append(item)
print(mylist)