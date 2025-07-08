def longest(strings: list):
	thelongest = ""
	for string in strings:
		if thelongest == "" or len(thelongest) < len(string):
			thelongest = string
	return thelongest

if __name__ == "__main__":
	strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
	print(longest(strings))