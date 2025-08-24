def filter_solutions():
	solutions_file = "solutions.csv"
	correct_file = "correct.csv"
	incorrect_file = "incorrect.csv"
	open(correct_file, "w").close()
	open(incorrect_file, "w").close()
	with open(solutions_file) as solutions:
		for line in solutions:
			tokens = line.split(";")
			result = int(tokens[2])
			addition = tokens[1].split("+")
			subtraction = tokens[1].split("-")
			operation = 0
			if len(addition) > 1:
				operation = int(addition[0]) + int(addition[1])
			if len(subtraction) > 1:
				operation = int(subtraction[0]) - int(subtraction[1])
			if operation != result:
				incorrect = open(incorrect_file, "a")
				incorrect.write(line)
			else:
				correct = open(correct_file, "a")
				correct.write(line)

if __name__ == "__main__":
	filter_solutions()