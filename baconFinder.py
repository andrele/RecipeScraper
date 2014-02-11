import simplejson as json

# Load file
f = open('recipeIngredients_baconTest.json', 'r')

# Import all recipes
recipes = json.load(f)



# Create list of ingredients
ingredients = []
# Loop through all recipes
for recipe in recipes:
	# Loop through recipe ingredient list
	for recipeIngredient in recipe.get("ingredients"):
		# For each ingredient, check to see if it exists in ingredients dictionary list
		foundIngredient = False;
		for ingredient in ingredients:
			if recipeIngredient not in ingredient:
				break
			else:
				ingredient[recipeIngredient].append(recipe.get("uid"))
				print("Added " + str(recipe.get("uid")) + " to " + recipeIngredient)
				foundIngredient = True
		if foundIngredient is False:
			print("New ingredient added: " + recipeIngredient)
			ingredients.append({ recipeIngredient: [recipe.get("uid")] })
print(ingredients)
# Find bacon in ingredients