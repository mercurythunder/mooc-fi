from math import *
from string import *

def change_case(orig_string: str):
	result_string = ""
	for char in orig_string:
		if char.isupper():
			result_string += char.lower()
		else:
			result_string += char.upper()
	return result_string

def split_in_half(orig_string: str):
	midpoint = floor(len(orig_string) / 2)
	return (orig_string[:midpoint], orig_string[midpoint:])

def remove_special_characters(orig_string: str):
	result_string = ""
	for char in orig_string:
		if char in ascii_letters or char in digits or char in whitespace:
			result_string += char
	return result_string