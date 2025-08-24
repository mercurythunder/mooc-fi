hourly = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")
if day != "Sunday":
	print(f"Daily wages: {hourly * hours} euros")
else:
	print(f"Daily wages: {hourly * hours * 2} euros")