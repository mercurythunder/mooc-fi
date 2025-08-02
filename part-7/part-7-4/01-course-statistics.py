from json import *
import urllib.request
from math import *

def retrieve_all():
	req = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
	data = loads(req.read())
	results = list()
	for entry in data:
		if entry["enabled"] is True:
			all_values = entry["exercises"]
			values = 0
			for value in all_values:
				values += value
			new_entry = (entry["fullName"], entry["name"], entry["year"], values)
			results.append(new_entry)
	return results

def retrieve_course(course_name: str):
	req = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
	data = loads(req.read())
	results = dict()
	results["weeks"] = len(data)
	max_students = 0
	total_hours = 0
	total_exercises = 0
	for entry in data:
		if int(data[entry]["students"]) > max_students:
			max_students = data[entry]["students"]
		total_hours += data[entry]["hour_total"]
		total_exercises += data[entry]["exercise_total"]
	results["students"] = max_students
	results["hours"] = total_hours
	results["hours_average"] = floor(total_hours / max_students)
	results["exercises"] = total_exercises
	results["exercises_average"] = floor(total_exercises / max_students)
	return results

if __name__ == "__main__":
	print(retrieve_all())
	print(retrieve_course("ofs2019"))