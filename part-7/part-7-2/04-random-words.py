from random import *

def words(n: int, beginning: str):
	word_list = list()
	all_words = list()
	current_words = 0
	file = open("words.txt")
	for line in file:
		if line.startswith(beginning):
			word_list.append(line.strip())
			current_words += 1
	if n > current_words:
		raise ValueError("Not enough matching words in the list")
	elif n == current_words:
		return word_list
	else:
		choice_list = list()
		choice_len = 0
		while choice_len < n:
			new_word = choice(word_list)
			if new_word not in choice_list:
				choice_list.append(new_word.strip())
				choice_len += 1
		return choice_list

if __name__ == "__main__":
	word_list = words(3, "ca")
	for word in word_list:
		print(word)