#! /usr/local/bin/python3
# bulledPointAdder.py - Fügt Sternchen vor einen Text aus der Zwischenablage hinzu

import pyperclip

text = pyperclip.paste()

lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = "* " + lines[i]
text = "\n".join(lines)

pyperclip.copy(text)
