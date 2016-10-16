#! /usr/local/bin/python3
# mcb.pyw - Speichert Text und lädt ihn in die Zwischenablage
# Nutzung: py.exe mcb.pyw save <Schlüssel> - Speichert den Inhalt
# der Zwischenablage unter dem Schlüssel
# py.exe mcb.pyw <Schlüssel> - Läd den Wert
# des Schlüssels in die Zwischenablage
# py.exe mcb.pyw list - Läd alle Schlüssel in die Zwischenablage
# py.exe mcb.pyw delete <schlüssel> - Löscht den entsprechenden Schlüssel
# py.exe mcb.pyw delete - Löscht alle Schlüssel



import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Inhalt der Zwischenablage speichern
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

    #  Schlüsselwörter auflisten und Inhalt laden
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # Löscht den gesamten Inhalt
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

# löschen einzelner elemente
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

mcbShelf.close()
