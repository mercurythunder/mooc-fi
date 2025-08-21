class Person:
	def __init__(self, name: str, height: int):
		self.name = name
		self.height = height

	def __str__(self):
		return f"{self.name} ({self.height} cm)"

class Room:
	def __init__(self):
		self.people = list()
	
	def add(self, person: Person):
		self.people.append(person)
	
	def is_empty(self):
		return len(self.people) == 0
	
	def print_contents(self):
		height = 0
		for person in self.people:
			height += person.height
		print(f"There are {len(self.people)} persons in the room, and their combined height is {height} cm")
		for person in self.people:
			print(person)

	def shortest(self):
		shortest = None
		height = -1
		for person in self.people:
			if person.height < height or height < 0:
				shortest = person
				height = person.height
		return shortest
	
	def remove_shortest(self):
		if len(self.people) == 0:
			return None
		shortest = self.shortest()
		self.people.remove(shortest)
		return shortest

if __name__ == "__main__":
	room = Room()
	room.add(Person("Lea", 183))
	room.add(Person("Kenya", 172))
	room.add(Person("Nina", 162))
	room.add(Person("Ally", 166))
	room.print_contents()
	print()
	removed = room.remove_shortest()
	print(f"Removed from room: {removed.name}")
	print()
	room.print_contents()