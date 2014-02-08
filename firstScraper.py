import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
		divs = divs.find_next("div", "hub-list-view")

