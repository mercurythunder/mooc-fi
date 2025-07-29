from random import *
from string import *

def generate_password(length: int):
	pool = ascii_lowercase
	password = ""
	for i in range(0, length):
		password += choice(pool)
	return password

if __name__ == "__main__":
	for i in range(10):
		print(generate_password(8))