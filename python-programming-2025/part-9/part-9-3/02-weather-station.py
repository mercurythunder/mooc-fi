class WeatherStation:
	def __init__(self, name: str):
		self.__name = name
		self.__observations = list()
	
	def __str__(self):
		return f"{self.__name}, {len(self.__observations)} observations"

	# @property
	# def name(self):
	#	return self.__name
	
	# @name.setter
	# def name(self, name: str):
	#	self.__name = name
	
	def add_observation(self, observation: str):
		self.__observations.append(observation)
	
	def latest_observation(self):
		if len(self.__observations) > 0:
			return self.__observations[-1]
		else:
			return ""
	
	def number_of_observations(self):
		return len(self.__observations)

if __name__ == "__main__":
	station = WeatherStation("Houston")
	station.add_observation("Rain 10mm")
	station.add_observation("Sunny")
	print(station.latest_observation())
	station.add_observation("Thunderstorm")
	print(station.latest_observation())
	print(station.number_of_observations())
	print(station)