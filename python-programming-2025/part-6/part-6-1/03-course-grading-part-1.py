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

def print_total_exercises(students: dict, exercises: dict):
	for student_id in exercises:
		exercises_total = 0
		exercise_list = exercises[student_id]
		for exercise in exercise_list:
			exercises_total += int(exercise)
		print(f"{students[student_id]} {exercises_total}")

students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
students_dict = read_students(students_file)
courses_dict = read_courses(exercises_file)
print_total_exercises(students_dict, courses_dict)