import os
import re

def GetFrequency(path):
    text = None
    letters = {}
    count = 0
    with open(path, "r") as f:
        text = f.read()
        text = re.sub(r"[^a-zA-Zа-яА-ЯЇї]", "", text)
        print(text)
    for letter in text:
        count += 1
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    s = 0
    for k, v in letters.items():
        letters[k] = v / count
        s += letters[k]
    print(count)
    print(letters)
    print(s)

GetFrequency("text.txt")
