def longest_series_of_neighbours(mylist):
	neighbours = 0
	highest = 0
	continuous = True
	latest = -1
	for item in mylist:
		if latest == -1:
			latest = item
		else:
			if abs(item - latest) == 1 and continuous:
				neighbours += 1
				if highest < neighbours:
					highest = neighbours
			elif abs(item - latest) == 1 and not continuous:
				continuous = True
				neighbours = 1
			else:
				neighbours = 0
			latest = item
	return highest + 1

if __name__ == "__main__":
	my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
	print(longest_series_of_neighbours(my_list))