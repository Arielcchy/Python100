# Find the Minimum Value in a Dictionary

s = {"a": 4, "b": 3, "c": 7}
# s = {}

if not s:
    print(None)
else:
    print(min(set(s.values())))

