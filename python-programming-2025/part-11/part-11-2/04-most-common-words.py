from re import *
from string import *

def most_common_words(filename: str, lower_limit: int):
	file = open(filename)
	occurrences = dict()
	for line in file:
		words = sub(r'[^\w\s]', '', line).split() # Regular expression to remove punctuation
		for word in words:
			if word in occurrences:
				occurrences[word] += 1
			else:
				occurrences[word] = 1
	return {word: occurrences[word] for word in occurrences if occurrences[word] >= lower_limit}

if __name__ == "__main__":
	print(most_common_words("comprehensions.txt", 3))