# This Python file uses the following encoding: utf-8

import sys
import time
import simplejson as json

reload(sys)
sys.setdefaultencoding("utf-8")

f = open("recipeIngredients_new.json", "a")

from bs4 import BeautifulSoup

import requests

for i in range(2,200):
	print("Page: " + str(i))
	# url = "allrecipes.com/recipes/breakfast-and-brunch/main.aspx?evt19=1&Page="+str(i)+"&vm=l&p34=HR_ListView#recipes"
	# url = "allrecipes.com/recipes/main-dish/main.aspx?evt19=1&Page="+str(i)+"&vm=l&p34=HR_ListView#recipes"
	url = "allrecipes.com/Recipes/World-Cuisine/Main.aspx?evt19=1&vm=l&p34=HR_ListView&Page="+str(i)
	r = requests.get("http://" +url)
	data = r.text
	soup = BeautifulSoup(data)

	divs = soup.find("div", "hub-list-view")
	while divs != None:
		header = divs.find("h3", "resultTitle")
		if header != None:
			# Create empty receipe object
			recipe = { }
			# Recipe Link
			link = header.a["href"]
			recipe["url"] = link
			req = requests.get(link)
			recipeData = req.text
			recipePage = BeautifulSoup(recipeData)
			# Start scraping recipe page here
			recipeId = recipePage.find("div", id = "zoneRecipe")
			uid = recipeId.get("data-typespecificid")
			recipe["uid"] = uid
			title = recipePage.find("h1", id = "itemTitle")
			recipe["name"] = title.string
			print("\n\n" + title.string + "[" + uid + "]")
			print(link)
			photo = recipePage.find("img", id = "imgPhoto")
			recipe["photo"] = photo.get("src")
			print(photo.get("src"))

			# Create empty ingredients list
			ingredients = [ ]
			names = recipePage.find_all("span", "ingredient-name")
			for name in names:
				if name.string != "" and name.string != " ":
					split = name.string.split(",")
					ingredient = split[0]
					ingredients.append(ingredient)
					# tokens = nltk.word_tokenize(ingredients)
					# print(tokens)
					# tagged = nltk.pos_tag(tokens)
					# f.write(ingredients+"\n")
					print(ingredient)
				names = recipePage.find_next("span", "ingredient-name")
			recipe["ingredients"] = ingredients
			jsonString = json.dumps(recipe) + ",\n"
			f.write(jsonString)
			print(jsonString)
		divs = divs.find_next("div", "hub-list-view")

