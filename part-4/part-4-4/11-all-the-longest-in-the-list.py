def all_the_longest(mylist):
	thelongest = list()
	for string in mylist:
		if len(thelongest) == 0:
			thelongest.append(string)
		else:
			latest = thelongest.pop()
			if len(latest) < len(string):
				del thelongest[:]
				thelongest.append(string)
			elif len(latest) == len(string):
				thelongest.append(latest)
				thelongest.append(string)
			else:
				thelongest.append(latest)
	return thelongest

if __name__ == "__main__":
	my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
	result = all_the_longest(my_list)
	print(result) # ['dorothy', 'richard']