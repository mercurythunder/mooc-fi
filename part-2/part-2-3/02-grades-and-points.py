grade = int(input("How many points [0-100]: "))
if grade < 0 or grade > 100:
	print("Grade: impossible!")
elif 0 <= grade < 50:
	print("Grade: fail")
elif 50 <= grade < 60:
	print("Grade: 1")
elif 60 <= grade < 70:
	print("Grade: 2")
elif 70 <= grade < 80:
	print("Grade: 3")
elif 80 <= grade < 90:
	print("Grade: 4")
else:
	print("Grade: 5")