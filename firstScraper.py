# This Python file uses the following encoding: utf-8

import json
import sys
import time
import nltk

from nltk.tokenize import word_tokenize

reload(sys)
sys.setdefaultencoding("utf-8")

f = open("recipeIngredients.txt", "w")

from bs4 import BeautifulSoup

import requests

for i in range(2,10):
	url = "allrecipes.com/recipes/breakfast-and-brunch/main.aspx?evt19=1&Page="+str(i)+"&vm=l&p34=HR_ListView#recipes"

	r = requests.get("http://" +url)
	data = r.text

	soup = BeautifulSoup(data)

	divs = soup.find("div", "hub-list-view")
	while divs != None:
		header = divs.find("h3", "resultTitle")
		if header != None:
			# Recipe Link
			link = header.a["href"]
			print(link)
			req = requests.get(link)
			recipeData = req.text
			recipePage = BeautifulSoup(recipeData)
			# Start scraping recipe page here
			title = recipePage.find("h1", id = "itemTitle")
			print(title.string)
			photo = recipePage.find("img", id = "imgPhoto")
			print(photo.get("src"))
			names = recipePage.find_all("span", "ingredient-name")
			for name in names:
				if name.string != "" and name.string != " ":
					split = name.string.split(",")
					ingredients = split[0]
					# tokens = nltk.word_tokenize(ingredients)
					# print(tokens)
					# tagged = nltk.pos_tag(tokens)
					# f.write(ingredients+"\n")
					print(ingredients)
				names = recipePage.find_next("span", "ingredient-name")

		divs = divs.find_next("div", "hub-list-view")

