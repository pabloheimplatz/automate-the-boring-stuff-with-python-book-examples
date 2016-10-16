from bs4 import BeautifulSoup

import requests

url = "https://de.pinterest.com/pabloheimplatz/family/"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

for css_class in soup.find_all("div", class_="item"):
    print(css_class.get('style'))
