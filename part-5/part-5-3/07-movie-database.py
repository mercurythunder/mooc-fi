def add_movie(database: list, name: str, director: str, year: int, runtime: int):
	movie = dict()
	movie["name"] = name
	movie["director"] = director
	movie["year"] = year
	movie["runtime"] = runtime
	database.append(movie)

if __name__ == "__main__":
	database = []
	add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
	add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
	print(database)