import re

with open(".txt") as f:
    txt = f.read()
x = re.search("[A-Z]{1}[a-z]+", txt)
print (x.string())
