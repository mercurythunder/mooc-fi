def oldest_person(people: list):
	oldest = None
	oldest_year = -1
	for person in people:
		if oldest_year < 0:
			oldest = person[0]
			oldest_year = person[1]
		else:
			if person[1] < oldest_year:
				oldest = person[0]
				oldest_year = person[1]
	return oldest

if __name__ == "__main__":
	p1 = ("Adam", 1977)
	p2 = ("Ellen", 1985)
	p3 = ("Mary", 1953)
	p4 = ("Ernest", 1997)
	people = [p1, p2, p3, p4]
	print(oldest_person(people))