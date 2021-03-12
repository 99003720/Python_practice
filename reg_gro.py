import re
pat = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pat, "abcdefghijkl")

if match:
    print(match.group("first"))
    print(match.groups())
