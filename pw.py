#! /usr/local/bin/python3
# pw.py - Passwortsafe Programm
import sys, pyperclip

PASSWORDS = {"email": "68fyYdnTbi8&",
             "blog": "UVHRn7^33/Ck",
             "luggage": "1234"}

if len(sys.argv) < 2:
    print ("Usage: >python3 pw.py [account] - to copy account password")
    sys.exit()

account = sys.argv[1]               # Das erste Befehlszeilenargument ist der Kontoname

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print ('Passwort for ' + account + ' copied to your clipboard.')
else:
    print('There is no account named ' + account)
