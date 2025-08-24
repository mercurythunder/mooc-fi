from difflib import *

def spellcheck(text: str, dictionary: str):
	corrected = ""
	wordlist = list()
	suggestions = dict()
	wrong_words = list()
	with open(dictionary) as file:
		for line in file:
			wordlist.append(line.lower().strip())
	first = True
	tokens = text.split()
	for token in tokens:
		if not first:
			corrected += " "
			if token.lower() not in wordlist:
				corrected += "*"
				corrected += token
				corrected += "*"
				wrong_words.append(token)
			else:
				corrected += token
		else:
			first = False
			if token.lower() not in wordlist:
				corrected += "*"
				corrected += token
				corrected += "*"
				wrong_words.append(token)
			else:
				corrected += token
	if len(wrong_words) > 0:
		for word in wrong_words:
			suggestions[word] = get_close_matches(word, wordlist)
	return (corrected, suggestions)

sentence = input("Write text: ")
results = spellcheck(sentence, "wordlist.txt")
print(results[0])
print("suggestions:")
words = results[1]
for word in words:
	sentence = word
	sentence += ": "
	for suggestion in words[word]:
		sentence += suggestion
		sentence += ", "
	sentence = sentence[:-2]
	print(sentence)