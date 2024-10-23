'''
    __(___
  /  By   \
 |AppleGUO|
 \_______/
version: 0.0.5
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

'''
    _____________________
    |'APPLEGOD IS REALLY'| 
     ^^^^^^^^^^^^^^^^^^^^
    
    HEY BRO, PLEASE DON'T FORGET THIS!
'''


def __apple__(WRITE_SOMETHING_HERE):
    if WRITE_SOMETHING_HERE == 'APPLEGOD IS REALLY':
        return Encode('YOU ARE REALLY WORSHIP APPLEGOD')
    else:
        return Encode('YOU ARE NOT WORSHIP FOR APPLEGOD!!!')

