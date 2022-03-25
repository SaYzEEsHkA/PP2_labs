import re

with open(".txt") as f:
    txt = f.read()
x = re.search('^[a-z]+_[a-z]+$', txt)
print (x.string())
