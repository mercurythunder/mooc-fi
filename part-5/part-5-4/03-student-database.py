def add_student(students: dict, student: str):
	students[student] = None

def print_student(students: dict, student: str):
	if student not in students:
		print(f"{student}: no such person in the database")
	elif students[student] == None:
		print(f"{student}:")
		print(" no completed courses")
	else:
		print(f"{student}:")
		print(f" {len(students[student])} completed courses:")
		average = 0.0
		for course in students[student]:
			if course[1] > 0:
				print(f"  {course[0]} {course[1]}")
				average += course[1]
		print(f" average grade {average / len(students[student])}")

def add_course(students: dict, student: str, course: tuple):
	if course[1] <= 0:
		return
	if student not in students or students[student] == None:
		students[student] = list()
	for pairs in students[student]:
		if pairs[0] == course[0]:
			if pairs[1] <= course[1]:
				students[student].remove(pairs)
				students[student].append(course)
			return
	students[student].append(course)

def summary(students: dict):
	print(f"students {len(students)}")
	most_courses = 0
	most_courses_student = None
	best_grade = 0.0
	best_grade_student = None
	for student in students:
		if(total_courses(students, student)) > most_courses:
			most_courses = total_courses(students, student)
			most_courses_student = student
		if(average_grade(students, student)) > best_grade:
			best_grade = average_grade(students, student)
			best_grade_student = student
	print(f"most courses completed {most_courses} {most_courses_student}")
	print(f"best average grade {best_grade} {best_grade_student}")

def total_courses(students: dict, student: str):
	if student in students:
		return len(students[student])
	else:
		return 0

def average_grade(students: dict, student: str):
	if student not in students or len(students[student]) <= 0:
		return 0.0
	average = 0.0
	for exam in students[student]:
		average += exam[1]
	return average / len(students[student])

if __name__ == "__main__":
	students = {}
	add_student(students, "Peter")
	add_student(students, "Eliza")
	add_course(students, "Peter", ("Data Structures and Algorithms", 1))
	add_course(students, "Peter", ("Introduction to Programming", 1))
	add_course(students, "Peter", ("Advanced Course in Programming", 1))
	add_course(students, "Eliza", ("Introduction to Programming", 5))
	add_course(students, "Eliza", ("Introduction to Computer Science", 4))
	summary(students)