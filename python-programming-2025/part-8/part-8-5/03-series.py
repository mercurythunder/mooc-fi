class Series:
	def __init__(self, title: str, seasons: int, genres: list):
		self.title = title
		self.seasons = seasons
		self.genres = genres
		self.ratings = list()
	
	def __str__(self):
		string = ""
		string += f"{self.title} ({str(self.seasons)} seasons)\n"
		all_genres = ", ".join(self.genres)
		string += f"genres: {all_genres}\n"
		if len(self.ratings) == 0:
			string += "no ratings"
		else:
			string += f"{len(self.ratings)} ratings, average {self.avg_ratings():.1f} points"
		return string

	def rate(self, rating: int):
		if 0 <= rating <= 5:
			self.ratings.append(rating)
	
	def avg_ratings(self):
		if len(self.ratings) == 0:
			return 0
		else:
			total_ratings = 0
			for rating in self.ratings:
				total_ratings += rating
			return total_ratings / len(self.ratings)
	
def minimum_grade(rating: float, series_list: list):
	series_above_rating = list()
	for series in series_list:
		if series.avg_ratings() >= rating:
			series_above_rating.append(series)
	return series_above_rating

def includes_genre(genre: str, series_list: list):
	series_including_genre = list()
	for series in series_list:
		for series_genre in series.genres:
			if genre == series_genre:
				series_including_genre.append(series)
	return series_including_genre

if __name__ == "__main__":
	dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	dexter.rate(4)
	dexter.rate(5)
	dexter.rate(5)
	dexter.rate(3)
	dexter.rate(0)
	print(dexter)
	s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	s1.rate(5)
	s2 = Series("South Park", 24, ["Animation", "Comedy"])
	s2.rate(3)
	s3 = Series("Friends", 10, ["Romance", "Comedy"])
	s3.rate(2)
	series_list = [s1, s2, s3]
	print("a minimum grade of 4.5:")
	for series in minimum_grade(4.5, series_list):
		print(series.title)
	print("genre Comedy:")
	for series in includes_genre("Comedy", series_list):
		print(series.title)