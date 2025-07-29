from random import *
from string import *

def generate_strong_password(length: int, numbers: bool, special: bool):
	pool = ascii_lowercase
	numbers_pool = "0123456789"
	special_chars_pool = "!?=+-()#"
	if numbers:
		pool += numbers_pool
	if special:
		pool += special_chars_pool
	password = ""
	contains_letter = False
	contains_numbers = False
	contains_special = False
	for i in range(0, length):
		new_character = choice(pool)
		password += new_character
		if new_character in ascii_lowercase:
			contains_letter = True
		if new_character in numbers_pool:
			contains_numbers = True
		if new_character in special_chars_pool:
			contains_special = True
	if contains_letter and ((numbers and contains_numbers) or (not numbers)) and ((special and contains_special) or (not special)):
		return password
	else:
		return generate_strong_password(length, numbers, special)

if __name__ == "__main__":
	for i in range(10):
		print(generate_strong_password(8, True, True))