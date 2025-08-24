story = ""
prevword = ""

while True:
	word = input("Please type in a word: ")
	if word == "end" or word == prevword:
		break
	story += word + " "
	prevword = word

print(story)