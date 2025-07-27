import re

def find_words(search_term: str):
	results = list()
	if search_term.endswith("*"):
		results = find_startswith(search_term.replace("*", ""), "words.txt")
	elif search_term.startswith("*"):
		results = find_endswith(search_term.replace("*", ""), "words.txt")
	else:
		results = find_contains(search_term, "words.txt")
	return results

def find_startswith(search_term: str, wordlist: str):
	words = open(wordlist)
	results = list()
	for word in words:
		if word.lower().strip().startswith(search_term.lower().strip()):
			results.append(word.strip())
	return results

def find_endswith(search_term: str, wordlist: str):
	words = open(wordlist)
	results = list()
	for word in words:
		if word.lower().strip().endswith(search_term.lower().strip()):
			results.append(word.strip())
	return results

def find_contains(search_term: str, wordlist: str):
	words = open(wordlist)
	results = list()
	length = len(search_term)
	pattern = re.escape(search_term).replace(r"\.", ".")
	regex = re.compile(pattern, re.IGNORECASE)
	for word in words:
		word_strip = word.strip()
		if (length == len(word_strip)) and regex.search(word_strip):
			results.append(word_strip)
	return results

if __name__ == "__main__":
	print(find_words("*vokes"))
	print(find_words("ka.a.e"))