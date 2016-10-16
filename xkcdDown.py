#! /usr/local/bin/python3
# Läd alle xkcd Comics herunter

import requests, os, bs4

url = 'https://xkcd.com' # start url
os.makedirs('xkcd', exist_ok=True) # speuchert die Comics in ./xkcd
while not url.endswith('#'):
    # Seite herunterladen
    print("Downloading page %s" % url)
    res = requests.get(url)
    res.raise_for_status() # check if download was fine

    soup = bs4.BeautifulSoup(res.text)

    # Bild auswählen und herunterladen
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicURL = comicElem[0].get('src')
        print(comicURL)

    # Läd das Bild herunter
    print("Downloading Image %s" % comicURL)
    res = requests.get('https:' + comicURL)
    res.raise_for_status()

    # Bild in ./xkcd speichern
    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # URL des Prev Buttons abrufen
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print("Done!")
