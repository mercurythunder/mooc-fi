limit = int(input("Limit: "))
iteration = 1
total = 0
report = "The consecutive sum: 1"
while total < limit:
	total += iteration
	if iteration > 1:
		report += f" + {iteration}"
	iteration += 1
report += f" = {total}"
print(report)