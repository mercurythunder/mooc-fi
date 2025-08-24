def cheaters():
	file_start = open("start_times.csv")
	start_times = dict()
	for line in file_start:
		data = line.split(";")
		name = data[0]
		timestamp = data[1].split(":")
		hour = int(timestamp[0])
		minute = int(timestamp[1])
		start_times[name] = hour * 60 + minute
	file_times = open("submissions.csv")
	cheaters = list()
	for line in file_times:
		data = line.split(";")
		name = data[0]
		timestamp = data[3].split(":")
		hour = int(timestamp[0])
		minute = int(timestamp[1])
		if name in start_times:
			if (hour * 60 + minute) > (int(start_times[name]) + 180):
				if name not in cheaters:
					cheaters.append(name)
	return cheaters

if __name__ == "__main__":
	print(cheaters())