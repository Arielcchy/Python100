# Find Frequency of Values in a Dictionary

# my_dict = {
#     "a": 4,
#     "b": 4,
#     "c": 2,
#     "d": 7,
#     "e": 4,
#     "f": 2,
#     "g": 7,
#     "h": 7
# }
my_dict = {}

freq_dict = {}
if not my_dict:
    print(my_dict)
else:
    for v in my_dict.values():
        if v in freq_dict:
            freq_dict[v] += 1
        else:
            freq_dict[v] = 1
    print(freq_dict)