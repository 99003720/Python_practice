import re

pat = r"g^r.y$"

if re.match(pat, "grey"):
    print("M1")
if re.match(pat, "gray"):
    print("M2")
if re.match(pat, "stingray"):
    print("M3")