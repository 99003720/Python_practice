import re
pat = r"(.+) \1"

match = re.match(pat,"word word")
if match:
    print("M1")
    match = re.match(pat, "?! ?!")
    if match:
        print("Match 2")
    
    match = re.match(pat,"abc cde")
    if match:
        print ("Match 3")
