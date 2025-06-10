value = float(input("Value of gift: "))
tax = 0.0

if value > 1000000:
	tax = tax + 142100 + ((value - 1000000) * 0.17)
elif value > 200000:
	tax = tax + 22100 + ((value - 200000) * 0.15)
elif value > 55000:
	tax = tax + 4700 + ((value - 55000) * 0.12)
elif value > 25000:
	tax = tax + 1700 + ((value - 25000) * 0.10)
elif value > 5000:
	tax = tax + 100 + ((value - 5000) * 0.08)

if tax == 0.0:
	print("No tax!")
else:
	print(f"Amount of tax: {tax} euros")