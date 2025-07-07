import string

def most_common_character(mystring):
	if len(mystring) <= 0:
		return None
	keymap = dict.fromkeys(string.ascii_lowercase, 0)
	for char in mystring:
		if char in keymap:
			keymap[char] += 1
	return max(keymap, key=keymap.get)

if __name__ == "__main__":
	first_string = "abcdbde"
	print(most_common_character(first_string))
	second_string = "exemplaryelementary"
	print(most_common_character(second_string))
	third_string = "no cap"
	print(most_common_character(third_string))