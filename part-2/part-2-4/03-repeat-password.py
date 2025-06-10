password = input("Password: ")

while True:
	newpassword = input("Repeat password: ")
	if password == newpassword:
		print("User account created!")
		break
	else:
		print("They do not match!")