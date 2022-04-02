# Merge Two Dictionaries

my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

# Update()
res = my_dict1.update(my_dict2)
print("1. update() won't generate a new dictionary: ", res )
print("1. update() modify the original dictionary: ", my_dict1)

# {**, **}
def Merge_asterisk(dic1, dic2):
    res = {**dic1, **dic2}
    return res
print("2. use ** to unpack the dictionary", Merge_asterisk(my_dict1,my_dict2))

# |
def Merge_line(dic1, dic2):
    res = dic1 | dic2
    return res
print("3. use | ", Merge_line(my_dict1,my_dict2))

# |=  update operator - won't generate a new dic
my_dict1 |= my_dict2
print("4. use |= ",  my_dict1)

# ChainMap
from collections import ChainMap
def Merge_ChainMap(dic1, dic2):
    res = ChainMap(dic1, dic2)
    return res
print("5. use collections module: ", Merge_ChainMap(my_dict1,my_dict2))

# https://peps.python.org/pep-0584/