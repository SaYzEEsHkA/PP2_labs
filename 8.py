import re

with open(".txt") as f:
    txt=f.read()

print(re.findall('[A-Z][^A-Z]*', txt))
