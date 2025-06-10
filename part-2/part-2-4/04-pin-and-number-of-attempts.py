pin = "4321"
tries = 0

while True:
	code = input("PIN: ")
	tries += 1
	if code == pin and tries == 1:
		print("Correct! It only took you one single attempt!")
		break
	elif code == pin:
		print(f"Correct! It took you {tries} attempts")
		break
	else:
		print("Wrong")