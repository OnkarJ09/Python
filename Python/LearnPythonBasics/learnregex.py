import re

txt = "there is raining in india"
x = re.search("^there.*india$", txt)

if x:
    print("Yes!there is")
else:
    print("No!")

