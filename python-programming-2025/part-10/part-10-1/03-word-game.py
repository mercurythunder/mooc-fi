import random

class WordGame():
	def __init__(self, rounds: int):
		self.wins1 = 0
		self.wins2 = 0
		self.rounds = rounds

	def round_winner(self, player1_word: str, player2_word: str):
		# determine a random winner
		return random.randint(1, 2)

	def play(self):
		print("Word game:")
		for i in range(1, self.rounds+1):
			print(f"round {i}")
			answer1 = input("player1: ")
			answer2 = input("player2: ")

			if self.round_winner(answer1, answer2) == 1:
				self.wins1 += 1
				print("player 1 won")
			elif self.round_winner(answer1, answer2) == 2:
				self.wins2 += 1
				print("player 2 won")
			else:
				pass # it's a tie

		print("game over, wins:")
		print(f"player 1: {self.wins1}")
		print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
	def __init__(self, rounds: int):
		super().__init__(rounds)
	
	def round_winner(self, player1_word: str, player2_word: str):
		if len(player1_word) == len(player2_word):
			return 0
		elif len(player1_word) > len(player2_word):
			return 1
		else:
			return 2

class MostVowels(WordGame):
	def __init__(self, rounds: int):
		super().__init__(rounds)
	
	def round_winner(self, player1_word: str, player2_word: str):
		vowels = "aeiouAEIOU"
		vowels_1 = 0
		vowels_2 = 0
		for char in player1_word:
			if char in vowels:
				vowels_1 += 1
		for char in player2_word:
			if char in vowels:
				vowels_2 += 1
		if vowels_1 == vowels_2:
			return 0
		elif vowels_1 > vowels_2:
			return 1
		else:
			return 2

class RockPaperScissors(WordGame):
	def __init__(self, rounds: int):
		super().__init__(rounds)
	
	def round_winner(self, player1_word: str, player2_word: str):
		valid = ["rock", "paper", "scissors"]
		if (player1_word.lower() not in valid and player2_word.lower() not in valid) or (player1_word.lower() == player2_word.lower()):
			return 0
		elif (player1_word.lower() in valid and player2_word.lower() not in valid) or (player1_word.lower() == "rock" and player2_word.lower() == "scissors") or (player1_word.lower() == "scissors" and player2_word.lower() == "paper") or (player1_word.lower() == "paper" and player2_word.lower() == "rock"):
			return 1
		else:
			return 2

if __name__ == "__main__":
	# Test 1
	p = WordGame(3)
	p.play()
	# Test 2
	p = LongestWord(3)
	p.play()
	# Test 3
	p = RockPaperScissors(4)
	p.play()