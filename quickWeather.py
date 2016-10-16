#! /usr/local/bin/python3
# quickweather.py - Gibt die Wettervorhersage für den angegebenen Standort aus.

import json, requests, sys

# Standort ermitteln
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = " ".join(sys.argv[1:])
#print(location)

#JSON herunter laden

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=fd2cf62d69f4ebe1a03aa31c5d4e6f0d' % (location)
#print(url)
response = requests.get(url)
response.raise_for_status()

# JSON-Daten in Pyhton laden
weatherData = json.loads(response.text)
#Wettervorhersage ausgeben
w = weatherData['list']
print('current weather in %s is:' %(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print("Tomorrow:")
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print("Day after tomorrow:")
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
