#! /usr/local/bin/python3
# lucky.py Öffnet die ersten drei Google-Suchergebnisse

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get("https://www.google.de/search?q="+" ".join(sys.argv[1:]))
res.raise_for_status()

# Links abrufen
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Browsertabs öffnen
linkElems = soup.select('.r a')
numOpen = min(2, len(linkElems))
for i in range(numOpen):
    webbrowser.open_new("https://www.google.de" + linkElems[i].get('href'))
