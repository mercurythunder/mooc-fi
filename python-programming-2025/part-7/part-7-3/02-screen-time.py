from datetime import *

def record_screentime(filename: str, startdate: str, number_of_days: int, tv_time: list, computer_time: list, mobile_time: list):
	file = open(filename, "w")
	startdate_p = datetime.strptime(startdate, "%d.%m.%Y")
	enddate_p = startdate_p + timedelta(days=(number_of_days - 1))
	startdate_f = datetime.strftime(startdate_p, "%d.%m.%Y")
	enddate_f = datetime.strftime(enddate_p, "%d.%m.%Y")
	file.write(f"Time period: {startdate_f}-{enddate_f}\n")
	time_total = 0
	for times in tv_time:
		time_total += times
	for times in computer_time:
		time_total += times
	for times in mobile_time:
		time_total += times
	time_avg = time_total / number_of_days
	file.write(f"Total minutes: {time_total}\n")
	file.write(f"Average minutes: {time_avg}\n")
	for i in range(0, number_of_days):
		currentdate_p = startdate_p + timedelta(days=i)
		currentdate_f = datetime.strftime(currentdate_p, "%d.%m.%Y")
		file.write(f"{currentdate_f}: {tv_time[i]}/{computer_time[i]}/{mobile_time[i]}\n")

filename = input("Filename: ")
startdate = input("Starting date: ")
startdate_p = datetime.strptime(startdate, "%d.%m.%Y")
number_of_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
tv_time = list()
computer_time = list()
mobile_time = list()
for i in range(0, number_of_days):
	currentdate_p = startdate_p + timedelta(days=i)
	currentdate_f = datetime.strftime(currentdate_p, "%d.%m.%Y")
	tokens = input(f"Screen time {currentdate_f}: ")
	minutes = tokens.split(" ")
	tv_time.append(int(minutes[0]))
	computer_time.append(int(minutes[1]))
	mobile_time.append(int(minutes[2]))
record_screentime(filename, startdate, number_of_days, tv_time, computer_time, mobile_time)
print(f"Data stored in file {filename}")