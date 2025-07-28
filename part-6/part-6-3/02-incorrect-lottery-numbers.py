def filter_incorrect():
	lottery_file = "lottery_numbers.csv"
	new_file = "correct_numbers.csv"
	lottery_entries = open(lottery_file)
	open(new_file, "w").close() # Clears the contents of the destination file
	for entry in lottery_entries:
		tokens = entry.split(";")
		try:
			week = int(tokens[0][5:])
		except:
			continue
		numbers = tokens[1].split(",")
		if len(numbers) == 7:
			flag = True
			numbers[6] = numbers[6].strip() # Removes the newline character at the end of the entry
			found_numbers = list()
			for number in numbers:
				try:
					digit = int(number)
				except:
					flag = False # Prevents the current line from being written to the lottery database
					break
				if int(number) < 1 or int(number) > 39 or int(number) in found_numbers:
					flag = False
					break
				found_numbers.append(int(number))
			if flag == True:
				add_to_file = open(new_file, "a")
				add_to_file.write(entry)
				add_to_file.close()

if __name__ == "__main__":
	filter_incorrect()