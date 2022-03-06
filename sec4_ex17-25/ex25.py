# Good comparison of List, Set, Tuple, Dictionary:
# https://www.educative.io/edpresso/list-vs-tuple-vs-set-vs-dictionary-in-python

# set build-in type
# https://docs.python.org/3/library/stdtypes.html#set

set1 = {1,2,3,4}
set2 = {3,4,5,6}

# Option 1 - create a set to store it
intersection = set() # create a set; intersection = {} will be dictionary

for ele in set1:
    if ele in set2:
        intersection.add(ele)
print(intersection)

# Option 2 - intersection(set2, set3, ...)
print(set1.intersection(set2))

