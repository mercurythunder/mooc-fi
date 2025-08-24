class Car:
	def __init__(self):
		self.__petrol = 0
		self.__odometer = 0
	
	def __str__(self):
		return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"

	def fill_up(self):
		self.__petrol = 60
	
	def drive(self, km: int):
		if km > 0:
			driven = 0
			while driven < km:
				if self.__petrol <= 0:
					break
				driven += 1
				self.__odometer += 1
				self.__petrol -= 1

if __name__ == "__main__":
	car = Car()
	print(car)
	car.fill_up()
	print(car)
	car.drive(40)
	print(car)
	car.drive(50)
	print(car)
	car.fill_up()
	print(car)