def read_recipes(filename: str):
	recipes = dict()
	current_recipe_name = ""
	current_recipe_instructions = list()
	with open(filename) as file:
		for line in file:
			if line == "\n":
				recipes[current_recipe_name] = current_recipe_instructions
			elif line[0].isupper():
				current_recipe_name = line.strip()
				current_recipe_instructions = list() # Refreshes the instructions list
			elif line.strip().isdigit():
				current_recipe_instructions.append(int(line.strip()))
			else:
				current_recipe_instructions.append(line.strip())
	recipes[current_recipe_name] = current_recipe_instructions
	return recipes

def search_by_name(filename: str, word: str):
	recipes = read_recipes(filename)
	matching_recipes = list()
	for recipe in recipes:
		if word.lower() in recipe.lower():
			matching_recipes.append(recipe)
	return matching_recipes

def search_by_time(filename: str, prep_time: int):
	recipes = read_recipes(filename)
	matching_recipes = list()
	for recipe in recipes:
		if recipes[recipe][0] <= prep_time:
			recipe_match = recipe + ", preparation time " + str(recipes[recipe][0]) + " min"
			matching_recipes.append(recipe_match)
	return matching_recipes

def search_by_ingredient(filename: str, ingredient: str):
	recipes = read_recipes(filename)
	matching_recipes = list()
	for recipe in recipes:
		ingredients = recipes[recipe]
		number_of_ingredients = len(ingredients)
		for i in range(1, number_of_ingredients): # Skips the first item on the list, which is the preparation time
			if recipes[recipe][i].lower() == ingredient.lower():
				recipe_match = recipe + ", preparation time " + str(recipes[recipe][0]) + " min"
				matching_recipes.append(recipe_match)
	return matching_recipes

if __name__ == "__main__":
	found_recipes = search_by_name("recipes1.txt", "cake")
	for recipe in found_recipes:
		print(recipe)
	found_recipes = search_by_time("recipes1.txt", 20)
	for recipe in found_recipes:
		print(recipe)
	found_recipes = search_by_ingredient("recipes1.txt", "eggs")
	for recipe in found_recipes:
		print(recipe)