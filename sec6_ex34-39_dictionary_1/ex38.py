# Find the Maximum Value in a Dictionary

s = {"a": 8, "b": 8, "c": 15}
# s = {}

if len(s.values()) == 0: # if not s:  can work too
    print(None)
else:
    print(max(list(s.values())))
    # max(set()) can work too, benefit of set: remove duplicates