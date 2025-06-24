def same_chars(string, m, n):
	if (len(string) <= m or len(string) <= n):
		return False
	else:
		return string[m] == string[n]

if __name__ == "__main__":
	print(same_chars("coder", 1, 2))