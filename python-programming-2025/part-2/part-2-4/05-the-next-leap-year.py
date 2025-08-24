year = int(input("Year: "))
newyear = year + 1

while newyear % 4 != 0:
	newyear += 1
if newyear % 100 == 0 and newyear % 400 != 0:
	newyear += 4

print(f"The next leap year after {year} is {newyear}")