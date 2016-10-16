#! /usr/local/bin/python3
# phoneAndEmail.py findet Telefonummern und Email Adressen in der Zwischenablage

import pyperclip, re

phoneRegex = re.compile(r'''
    ((\d{4})(\s|[-])?(\d{7})|([+]\d{2}\s?\d+\s?\d+) # für deutsche Handynummern
    )''', re.VERBOSE)

emailRegex = re.compile(r'''
    ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+[.][a-zA-Z0-9._%+-]+ # für Emailadressen
    )''', re.VERBOSE)

# Findet übereinstimmungen und kopiert diese in die Zwischenablage
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    matches.append(groups[0])
for groups in emailRegex.findall(text):
    matches.append(groups)
    #print (matches)

# Ergebnisse in die Zwischenablage kopieren
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no pphone numbers or mail adresses found.')

# kjsdfkjsdjfkdsfldkdsjfordsa fotos@pabloheimplatz.de lksdjfklsdjfklsdjdslk
# kdsfnflkdjflksd 01703480787. Aber auch (/(/)&%&/%)?= Hello_24@pabloheimplatz.com sollte zu finden sein.
# Genau so wie meine Nummer: +491703480787
