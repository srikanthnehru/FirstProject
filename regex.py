import re

s = input("Is it ok?")

if re.search("^y.*",s,re.IGNORECASE):
    print("Agreed")
else:
    print("not agreed")
#feature1_branch1
if re.search("^ok",s,re.IGNORECASE):
    print("Agreed")
else:
    print("not agreed")

