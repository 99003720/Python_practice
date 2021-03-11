import re

pat = r"g^r.y$"

if re.match(pat, "grey"):
    print("M1")
if re.match(pat, "gray"):
    print("M2")
if re.match(pat, "stingray"):
    print("M3")

pat = r"ice(-)?cream"

if re.match(pat, "ice-cream"):
    print("M1")
if re.match(pat, "icecream"):
    print("M2")
if re.match(pat, "ice--ice"):
    print("M3")
if re.match(pat, "sausages"):
    print("M3")
