import math

def get_station_data(filename: str):
	stations = dict()
	with open(filename) as file:
		for line in file:
			if line[0].isupper():
				continue
			tokens = line.strip().split(";")
			stations[tokens[3]] = (float(tokens[0]), float(tokens[1]))
	return stations

def distance(stations: dict, station1: str, station2: str):
	longitude1 = float(stations[station1][0])
	latitude1 = float(stations[station1][1])
	longitude2 = float(stations[station2][0])
	latitude2 = float(stations[station2][1])
	x_km = (longitude1 - longitude2) * 55.26
	y_km = (latitude1 - latitude2) * 111.2
	distance_km = math.sqrt(x_km ** 2 + y_km ** 2)
	return distance_km

def greatest_distance(stations: dict):
	longest_distance = 0.0
	station1 = ""
	station2 = ""
	all_stations = len(stations)
	for station_a in stations:
		for station_b in stations:
			if distance(stations, station_a, station_b) > longest_distance:
				longest_distance = distance(stations, station_a, station_b)
				station1 = station_a
				station2 = station_b
	return (station1, station2, float(longest_distance))

if __name__ == "__main__":
	stations = get_station_data("stations1.csv")
	d = distance(stations, "Designmuseo", "Hietalahdentori")
	print(d)
	d = distance(stations, "Viiskulma", "Kaivopuisto")
	print(d)
	stations = get_station_data("stations1.csv")
	station1, station2, greatest = greatest_distance(stations)
	print(station1, station2, greatest)