#! /usr/local/bin/python3
# Läd alle Bilder eines Instagram Accounts herunter

import requests, os, bs4

def InstaDwonload(usrName, count):
    url = ("https://www.instagram.com/" + usrName +"/") #startURL
    os.makedirs(usrName+'_Photos', exist_ok=True) #erzeugt einen Ordner mit (usrName)_Photos

    # Seite herunterladen
    print("Downloading page %s" % url)
    res = requests.get(url)
    res.raise_for_status() # check if download was fine

    #res.text.encode('utf-8').decode('ascii', 'ignore')
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    #print(res.content)

    #a class _8mlbc _vbtk2 _t5r8b search
    htmlsoup = soup.find_all("a", class_="_8mlbc _vbtk2 _t5r8b")
    print(htmlsoup)

    #firstImg = soup.select('div')
    if htmlsoup == []:
        print("Ups, no Images here, sorry!")
    else:
        lightboxURL = htmlsoup[1].get('href')
        print(lightboxURL)

InstaDwonload("pabloheimplatz", 2)
