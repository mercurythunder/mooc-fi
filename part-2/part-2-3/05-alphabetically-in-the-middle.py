a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")
if (a <= b and b <= c) or (c <= b and b <= a):
	print(f"The letter in the middle is {b}")
elif (a <= c and c <= b) or (b <= c and c <= a):
	print(f"The letter in the middle is {c}")
else:
	print(f"The letter in the middle is {a}")