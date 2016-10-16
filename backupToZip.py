#! /usr/local/bin/python3
# backupToZip.py - Kopiert einen und seinen gesamten Inhalt in eine
# ZIP- Datei mit laufender Nummerierung

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    # Name der aktuellen Zip Datei ermitteln
    number = 1
    while True:
        zipFilename = os.path.basename(folder + '_' + str(number) + '.zip')
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Zip Datei erstellen
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Den Verzeichnissbaum, durchlaufen und alle Dateien in allen Ordnen komprimieren.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Fuegt den aktuellen Ordner hinzu
        for filename in filenames:
            newBase / os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # dont backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')

backupToZip(('~/Desktop/tmp'))
