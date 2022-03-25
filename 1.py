import re

txt = {
    "ababb"
    "abb"
    "aasds"
    "abab"
}
x = re.search("^a*b", txt)
print (x.string())
