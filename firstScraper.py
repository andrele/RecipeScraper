# This Python file uses the following encoding: utf-8

import json
import sys
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
			link = header.a["href"]
			print(link)
			req = requests.get(link)
			recipeData = req.text
			recipePage = BeautifulSoup(recipeData)
			names = recipePage.find_all("span", "ingredient-name")
			for name in names:
				if name.string != "" and name.string != " ":
					split = name.string.split(",")
					f.write(split[0]+"\n")
					print(split[0])
				names = recipePage.find_next("span", "ingredient-name")

		divs = divs.find_next("div", "hub-list-view")

