import Applecode as ac
text = ac.Encode('This is a TEST.')
print(text)
text = ac.Unencode(text)
print(text)
