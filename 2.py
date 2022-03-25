import re

with open(".txt") as f:
    txt=f.read()
x=re.search("^a{2,3}b", txt)
print(x.string())
