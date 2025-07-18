def read_students(filename: str):
	students = dict()
	with open(filename) as file:
		for line in file:
			line_split = line.strip().split(";")
			if line_split[0] == "id":
				continue
			students[line_split[0]] = str(line_split[1]) + " " + str(line_split[2])
	return students

def read_courses(filename: str):
	courses = dict()
	with open(filename) as file:
		for line in file:
			line_split = line.strip().split(";")
			if line_split[0] == "id":
				continue
			courses[line_split[0]] = list()
			for i in range(1, len(line_split)):
				courses[line_split[0]].append(line_split[i])
	return courses

def read_points(filename: str):
	points = dict()
	with open(filename) as file:
		for line in file:
			line_split = line.strip().split(";")
			if line_split[0] == "id":
				continue
			grades[line_split[0]] = list()
			for i in range(1, len(line_split)):
				grades[line_split[0]].append(line_split[i])
	return points

def calculate_grade(exam_points: int, exercise_points: int):
	grade = exam_points + ((exercise_points) // 4)
	if grade <= 14:
		return 0
	elif 15 <= grade <= 17:
		return 1
	elif 18 <= grade <= 20:
		return 2
	elif 21 <= grade <= 23:
		return 3
	elif 24 <= grade <= 27:
		return 4
	else:
		return 5

def print_statistics(students: dict, exercises: dict, points: dict):
	name = "name"
	exec_nbr = "exec_nbr"
	exec_pts = "exec_pts."
	exm_pts = "exm_pts."
	tot_pts = "tot_pts."
	score = "grade"
	print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{score:10}")
	for student_id in exercises:
		exercises_total = 0
		exercise_list = exercises[student_id]
		for exercise in exercise_list:
			exercises_total += int(exercise)
		exams_total = 0
		exams_list = points[student_id]
		for exam in exams_list:
			exams_total += int(exam)
		grade = calculate_grade(exams_total, exercises_total)
		print(f"{students[student_id]:30}{exercises_total:<10}{(exercises_total // 4):<10}{exams_total:<10}{((exercises_total // 4) + exams_total):<10}{grade:<10}")

students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
points_file = input("Exam points: ")
students_dict = read_students(students_file)
courses_dict = read_courses(exercises_file)
points_dict = read_courses(points_file)
print_statistics(students_dict, courses_dict, points_dict)