def spellcheck(text: str, dictionary: str):
	corrected = ""
	wordlist = set()
	with open(dictionary) as file:
		for line in file:
			wordlist.add(line.lower().strip())
	first = True
	tokens = text.split()
	for token in tokens:
		if not first:
			corrected += " "
			if token.lower() not in wordlist:
				corrected += "*"
				corrected += token
				corrected += "*"
			else:
				corrected += token
		else:
			first = False
			if token.lower() not in wordlist:
				corrected += "*"
				corrected += token
				corrected += "*"
			else:
				corrected += token
	return corrected

sentence = input("Write text: ")
print(spellcheck(sentence, "wordlist.txt"))