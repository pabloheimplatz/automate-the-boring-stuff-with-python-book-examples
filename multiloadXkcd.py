#! /usr/local/bin/python3
# Laed alle xkcd Comics herunter (multithreading

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) # speuchert die Comics in ./xkcd
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Seite herunterladen
        print("Downloading page %s" % urlNumber)
        res = requests.get('https://xkcd.com/%s' %(urlNumber))
        res.raise_for_status() # check if download was fine

        soup = bs4.BeautifulSoup(res.text)

        # Bild auswaehlen und herunterladen
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image.")
        else:
            comicURL = comicElem[0].get('src')
            print(comicURL)
            # Laed das Bild herunter
            print("Downloading Image %s" % comicURL)
            res = requests.get('https:' + comicURL)
            res.raise_for_status()

            # Bild in ./xkcd speichern
            imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Erstellt und startet Thread-Objekte
downloadThreads = [] # Liste aller Thread-Objekte
for i in range(0, 1400, 100):     #laeuft 14 mal und erstellt 14 Threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i +99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wartet bis alle Threads beendet sind
for downloadThread in downloadThreads:
    downloadThread.join()
print("Done!")
