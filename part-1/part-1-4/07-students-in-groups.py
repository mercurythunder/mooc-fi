students = int(input("How many students on the course? "))
maxsize = int(input("Desired group size? "))
remainder = 0
if students % maxsize > 0:
	remainder = 1
print(f"Number of groups formed: {(students // maxsize + remainder)}")