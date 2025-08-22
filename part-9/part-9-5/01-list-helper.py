class ListHelper:
	@classmethod
	def greatest_frequency(cls, my_list: list):
		instances = dict()
		for item in my_list:
			if item in instances:
				instances[item] += 1
			else:
				instances[item] = 1
		greatest_number = 0
		most_frequent_item = ""
		for instance in instances:
			if instances[instance] > greatest_number:
				greatest_number = instances[instance]
				most_frequent_item = instance
		return most_frequent_item
	
	@classmethod
	def doubles(cls, my_list: list):
		instances = dict()
		items_doubled = 0
		for item in my_list:
			if item in instances:
				instances[item] += 1
				if instances[item] == 2:
					items_doubled += 1
			else:
				instances[item] = 1
		return items_doubled

if __name__ == "__main__":
	numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
	print(ListHelper.greatest_frequency(numbers))
	print(ListHelper.doubles(numbers))