def add_word(fin_word: str, eng_word: str, dictionary: str):
	file = open(dictionary, "a")
	entry = fin_word + " - " + eng_word
	file.write(entry)
	file.write("\n")
	print("Dictionary entry added")

def search_word(word: str, dictionary: str):
	file = open(dictionary)
	results = list()
	term = word.lower()
	for line in file:
		if term in line.lower():
			results.append(line)
	return results

while True:
	print("1 - Add word, 2 - Search, 3 - Quit")
	function = int(input("Function: "))
	if function == 1:
		fin_word = input("The word in Finnish: ")
		eng_word = input("The word in English: ")
		add_word(fin_word, eng_word, "dictionary.txt")
	elif function == 2:
		word = input("Search term: ")
		results = search_word(word, "dictionary.txt")
		for line in results:
			print(line)
	elif function == 3:
		print("Bye!")
		break
	else:
		print("Unknown command")