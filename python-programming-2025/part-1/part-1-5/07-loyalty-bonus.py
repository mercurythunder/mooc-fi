points = int(input("How many points are on your card? "))
bonus = 1.1
if points < 100:
	print("Your bonus is 10 %")
if points >= 100:
	bonus = 1.15
	print("Your bonus is 15 %")
print(f"You now have {points * bonus} points")