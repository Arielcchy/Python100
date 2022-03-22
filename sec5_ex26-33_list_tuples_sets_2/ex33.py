from itertools import permutations as p
# https://docs.python.org/3/library/itertools.html#itertools.permutations

s = [1,2,3]

for x in p(s, r=2):
    print(list(x))



