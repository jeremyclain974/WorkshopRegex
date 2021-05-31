import re

with open("exo2.txt", "r") as file:
    txt = file.read()

rgx = re.compile("(main : {[^\\}]*})")
res = rgx.findall(txt)
for i in res:
    print(i, end = '')
print()