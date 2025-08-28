class Course:
	def __init__(self, name: str, grade: int, credit_points: int):
		self.__name = name
		self.__grade = grade
		self.__credit_points = credit_points
	
	def __str__(self):
		return f"{self.name} ({self.credit_points} cr) grade {self.grade}"

	@property
	def name(self):
		return self.__name
	
	@property
	def grade(self):
		return self.__grade
	
	@property
	def credit_points(self):
		return self.__credit_points
	
	@grade.setter
	def grade(self, grade: int):
		self.__grade = grade
	
	@credit_points.setter
	def credit_points(self, credit_points: int):
		self.__credit_points = credit_points

class CourseCollection:
	def __init__(self):
		self.__courses = {}
	
	@property
	def courses(self):
		return self.__courses
	
	def add_course(self, name: str, grade: int, credit_points: int):
		if (name not in self.courses) or (name in self.courses and grade > self.courses[name].grade):
			self.courses[name] = Course(name, grade, credit_points)
	
	def get_course(self, name: str):
		if name in self.courses:
			return self.courses[name]
		else:
			return None
	
	def statistics(self):
		completed_courses = len(self.courses)
		total_credit_points = 0
		grade_distribution = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
		total_grade_points = 0
		for course in self.courses:
			total_credit_points += self.courses[course].credit_points
			if self.courses[course].grade == 1:
				grade_distribution["1"] += 1
				total_grade_points += 1
			elif self.courses[course].grade == 2:
				grade_distribution["2"] += 1
				total_grade_points += 2
			elif self.courses[course].grade == 3:
				grade_distribution["3"] += 1
				total_grade_points += 3
			elif self.courses[course].grade == 4:
				grade_distribution["4"] += 1
				total_grade_points += 4
			else:
				grade_distribution["5"] += 1
				total_grade_points += 5
		mean = total_grade_points / completed_courses
		return [completed_courses, total_credit_points, mean, grade_distribution]

class CourseApplication:
	def __init__(self):
		self.__course_collection = CourseCollection()
	
	@property
	def course_collection(self):
		return self.__course_collection

	def help(self):
		print("1 add course")
		print("2 get course data")
		print("3 statistics")
		print("0 exit")

	def add_course(self):
		name = input("course: ")
		grade = int(input("grade: "))
		credit_points = int(input("credits: "))
		self.course_collection.add_course(name, grade, credit_points)

	def get_course(self):
		name = input("course: ")
		course = self.course_collection.get_course(name)
		if course == None:
			print("no entry for this course")
		else:
			print(course)
	
	def statistics(self):
		information = self.course_collection.statistics()
		print(f"{information[0]} completed courses, a total of {information[1]} credits")
		print(f"mean {round(information[2], 1)}")
		print("grade distribution")
		print(f"5: {information[3]["5"] * "x"}")
		print(f"4: {information[3]["4"] * "x"}")
		print(f"3: {information[3]["3"] * "x"}")
		print(f"2: {information[3]["2"] * "x"}")
		print(f"1: {information[3]["1"] * "x"}")
	
	def execute(self):
		self.help()
		while True:
			print("")
			command = input("command: ")
			if command == "0":
				break
			elif command == "1":
				self.add_course()
			elif command == "2":
				self.get_course()
			elif command == "3":
				self.statistics()
			else:
				self.help()

course_collection = CourseApplication()
course_collection.execute()