#! /usr/local/bin/python3
# renameDates.py - Ändert amerikanische MM-DD-YYYY Daten ins europäische Format DD-MM-YYYY.

import shutil, os, re

# regex für Dateinamen mit US Angaben für das Datum.
datePattern = re.compile(r"""^(.*?) # Text vor dem Datum
    ((0|1)?\d)-                     # 1-2 Ziffern für MM
    ((0|1|2|3)?\d)-                 # 1-2 Ziffern für DD
    ((19|20)\d\d)                   # Vier Ziffern für YYYY
    (.*?)$                          # Text nach dem Datum
    """, re.VERBOSE)

# Alle Dateien im Arbeitsverzeichnis durchsuchen
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Dateinahmen ohne Datumsangabe überspringen
    if mo == None:
        continue
    # Die einzelnen Teile des Dateiformates abrufen
    beforePart  = mo.group(1)
    monthPart   = mo.group(2)
    dayPart     = mo.group(4)
    yearPart    = mo.group(6)
    afterPart   = mo.group(8)

    # Dateinamen im europäischen Format zusammenstellen
    euroFilename = beforePart + dayPart + monthPart + yearPart + afterPart

    # den kompletten absoluten Pfad abrufen
    absWorkDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkDir, amerFilename)
    euroFilename = os.path.join(absWorkDir, euroFilename)

    # Dateien umbenennen
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename) # Nach dem Test entkommentieren
