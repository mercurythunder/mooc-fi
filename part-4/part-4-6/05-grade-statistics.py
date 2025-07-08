def points(exam, exercise_points):
	return exam + (exercise_points // 10)

def grade(score, fail):
	if score <= 14 or fail == True:
		return 0
	elif score <= 17:
		return 1
	elif score <= 20:
		return 2
	elif score <= 23:
		return 3
	elif score <= 27:
		return 4
	else:
		return 5

def print_stats(all_scores, all_grades):
	average = round(sum(all_scores) / len(all_scores), 1)
	passed = 0
	grade_occurrences = dict()
	for grade in all_grades:
		if grade > 0:
			passed += 1
		if grade in grade_occurrences:
			grade_occurrences[grade] += 1
		else:
			grade_occurrences[grade] = 1
	pass_rate = round((passed / len(all_scores)) * 100, 1)
	print("Statistics:")
	print(f"Points average: {average}")
	print(f"Pass percentage: {pass_rate}")
	print("Grade distribution:")
	if 5 in grade_occurrences:
		print(" 5: " + "*" * grade_occurrences[5])
	else:
		print(" 5:")
	if 4 in grade_occurrences:
		print(" 4: " + "*" * grade_occurrences[4])
	else:
		print(" 4:")
	if 3 in grade_occurrences:
		print(" 3: " + "*" * grade_occurrences[3])
	else:
		print(" 3:")
	if 2 in grade_occurrences:
		print(" 2: " + "*" * grade_occurrences[2])
	else:
		print(" 2:")
	if 1 in grade_occurrences:
		print(" 1: " + "*" * grade_occurrences[1])
	else:
		print(" 1:")
	if 0 in grade_occurrences:
		print(" 0: " + "*" * grade_occurrences[0])
	else:
		print(" 0:")

def build_lists():
	scores = list()
	grades = list()
	while True:
		pair = input("Exam points and exercises completed: ")
		if pair != "":
			data = pair.split()
			current_score = scores.append(points(int(data[0]), int(data[1])))
			if int(data[0]) < 10:
				grades.append(0)
			else:
				grades.append(grade(points(int(data[0]), int(data[1])), False))
		else:
			break
	print_stats(scores, grades)

build_lists()