
pat = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghijkl")

if match:
    print(match.group("first"))
    print(match.groups())