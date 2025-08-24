from datetime import *

def age_at_eve(day: int, month: int, year: int):
	if year >= 2000:
		print("You weren't born yet on the eve of the new millennium.")
	else:
		time_eve = datetime(1999, 12, 31)
		time_birth = datetime(year, month, day)
		difference = time_eve - time_birth
		print(f"You were {difference.days} days old on the eve of the new millennium.")

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
age_at_eve(day, month, year)