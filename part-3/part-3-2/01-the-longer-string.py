s1 = input("Please type in string 1: ")
s2 = input("Please type in string 2: ")
ls1 = len(s1)
ls2 = len(s2)
if ls1 == ls2:
	print("The strings are equally long")
elif ls1 > ls2:
	print(f"{s1} is longer")
else:
	print(f"{s2} is longer")