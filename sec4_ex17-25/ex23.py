s = [1,2,4,4,5,1,3,1]
# s = ["a","a","b","a"]
# s = [1,3,2]
# s = []

# # Option 1 - dictionary, mutated the original list
# s.sort()
# print(s)

# dict_s = {}
# for ele in s:
#     if ele in dict_s.keys():
#         dict_s[ele] += 1
#     else:
#         dict_s[ele] = 1

# for key, x in dict_s.items():
#     if x > 1:
#         for i in range(1,x):
#             s.remove(key)
# print(s)

# # Option 2 - set() - mess up the order, create the other list
# no_duplicates = list(set(s))
# print(no_duplicates)

# Option 2 - dictionary - keep the order, create the other list
no_duplicates = list(dict.fromkeys(s))
print(no_duplicates)

