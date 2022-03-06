s = [9,8,7,10]

# # Option 1 - count()
# s.sort()
# greater_than_three = 0
# for i, ele in enumerate(s):
#     if ele > 3:
#         greater_than_three = len(s)-i
#         break

# print(greater_than_three)

# # Option 2 - dictionary
# dict_count = {}
# greater_than_three = 0
# for x in s:
#     if x in dict_count:
#         dict_count[x] += 1
#     else:
#         dict_count.update({x: 1})
# for ele, num in dict_count.items():
#     if ele > 3:
#         greater_than_three += num

# print(greater_than_three)

# Option 3 - set()

# Option 4 - 1 line code - Generator expression
count = sum(1 for x in s if x > 3)
print(count)