'''
    __(___
  /  By   \
 |AppleGUO|
 \_______/
version: 0.0.3
\(OvO)/ I can give you apple -> 🍎
'''
import random


def Encode(text):
    l = list(text)
    for i in range(len(l) - 2):
        l.insert(random.randrange(1, len(l)), '🍎')
    text = ''
    for i in range(len(l)):
        text = f'{text}{l[i]}'
        i += 1
    return text

def Unencode(text):
    return text.replace('🍎', '')