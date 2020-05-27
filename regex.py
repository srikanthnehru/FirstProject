import re

s = input("Is it ok?")

if re.search("^y.*",s,re.IGNORECASE):
    print("Agreed")
else:
    print("not agreed")

if re.search("^y.*",s,re.IGNORECASE):
    print("Agreed")
else:
    print("not agreed")