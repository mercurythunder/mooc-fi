def histogram(word: str):
	chars = dict()
	for char in word:
		if char not in chars:
			chars[char] = 1
		else:
			chars[char] += 1
	for char in chars:
		print(f"{char} {'*' * chars[char]}")

if __name__ == "__main__":
	histogram("abba")
	histogram("xylophone")
	histogram("australia")
	histogram("kamaljiori")