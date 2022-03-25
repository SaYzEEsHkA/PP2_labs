import re

with open(".txt") as f:
    txt = f.read()
x = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
print (re.sub('([a-z0-9])([A-Z])', r'\1_\2', x).lower())
