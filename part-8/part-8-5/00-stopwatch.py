class Stopwatch:
	def __init__(self):
		self.seconds = 0
		self.minutes = 0
	
	def __str__(self):
		mins = ""
		secs = ""
		if self.minutes < 10:
			mins += "0"
		mins += str(self.minutes)
		if self.seconds < 10:
			secs += "0"
		secs += str(self.seconds)
		return f"{mins}:{secs}"

	def tick(self):
		if self.seconds < 59:
			self.seconds += 1
		elif self.minutes < 59:
			self.seconds = 0
			self.minutes += 1
		else:
			self.seconds = 0
			self.minutes = 0

if __name__ == "__main__":
	watch = Stopwatch()
	for i in range(3600):
		print(watch)
		watch.tick()