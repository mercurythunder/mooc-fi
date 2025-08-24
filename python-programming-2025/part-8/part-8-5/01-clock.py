class Clock:
	def __init__(self, hours: int, minutes: int, seconds: int):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
	
	def __str__(self):
		hrs = ""
		mins = ""
		secs = ""
		if self.hours < 10:
			hrs += "0"
		hrs += str(self.hours)
		if self.minutes < 10:
			mins += "0"
		mins += str(self.minutes)
		if self.seconds < 10:
			secs += "0"
		secs += str(self.seconds)
		return f"{hrs}:{mins}:{secs}"

	def tick(self):
		if self.seconds < 59:
			self.seconds += 1
		elif self.minutes < 59:
			self.seconds = 0
			self.minutes += 1
		elif self.hours < 23:
			self.seconds = 0
			self.minutes = 0
			self.hours += 1
		else:
			self.seconds = 0
			self.minutes = 0
			self.hours = 0
	
	def set(self, hours: int, minutes: int):
		self.hours = hours
		self.minutes = minutes
		self.seconds = 0

if __name__ == "__main__":
	clock = Clock(23, 59, 55)
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.set(12, 5)
	print(clock)