def palindromes(string):
	return string[::-1] == string

while True:
	string = input("Please type in a palindrome: ")
	if(palindromes(string)):
		print(f"{string} is a palindrome!")
		break
	else:
		print("that wasn't a palindrome")