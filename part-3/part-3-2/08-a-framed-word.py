import math

word = input("Word: ")
letters = len(word)
sentence = ""
print("*" * 30)
sentence += "*"
sentence += " " * math.ceil((28 - letters) / 2)
sentence += word
sentence += " " * math.floor((28 - letters) / 2)
sentence += "*"
print(sentence)
print("*" * 30)