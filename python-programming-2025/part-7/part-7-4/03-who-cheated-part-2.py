def final_points():
	points = dict() # Key: student | Value: total points
	file_start = open("start_times.csv")
	start_times = dict() # Key: student | Value: start time of the tasks in minutes
	for line in file_start:
		data = line.split(";")
		name = data[0]
		timestamp = data[1].split(":")
		hour = int(timestamp[0])
		minute = int(timestamp[1])
		start_times[name] = hour * 60 + minute
	file_times = open("submissions.csv")
	tasks = dict() # Key: student | Value: nested dictionary || Key: task number || Value: task points
	for line in file_times:
		data = line.split(";")
		name = data[0]
		current_task = int(data[1])
		task_points = int(data[2])
		timestamp = data[3].split(":")
		hour = int(timestamp[0])
		minute = int(timestamp[1])
		if name in start_times:
			if (hour * 60 + minute) <= (int(start_times[name]) + 180):
				added_points = 0
				if name not in tasks: # The student has not yet been added to the tasks dictionary
					tasks[name] = dict()
					tasks[name][current_task] = task_points
					added_points = task_points
				else: # The student is already in the tasks dictionary; check if the task points need to be updated
					if current_task not in tasks[name]:
						tasks[name][current_task] = task_points
						added_points = task_points
					else:
						if task_points > tasks[name][current_task]:
							added_points = task_points - tasks[name][current_task]
							tasks[name][current_task] = task_points
				if name not in points: # The student has not yet been added to the points dictionary
					points[name] = added_points
				else:
					points[name] += added_points
	return points

if __name__ == "__main__":
	print(final_points())