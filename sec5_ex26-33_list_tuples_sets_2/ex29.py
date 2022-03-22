s = [1,2]

# # Option 1 - sort(reverse), compare from the first element
# s.sort(reverse=True) # or s_sorted = sorted(s)
# # https://www.programiz.com/python-programming/methods/list/sort
# if len(s) > 1:
#     for i in range(0,len(s)-1):
#         # print(i)
#         if s[i] > s[i+1]: # if every element only exist once: s_sorted[-2]
#             print(s[i+1])
#             break
# else:
#     print(None)

# # Option 2 - sort(), compare from the last element
# s.sort()
# if len(s) > 1:
#     for i in range(len(s)-1, 0, -1):
#         # print(i)
#         if s[i] > s[i-1]:
#             print(s[i-1])
#             break
# else:
#     print(None)

# Option 3 - set(), remove(max)
if len(s) > 1:
    s_no_duplicated = set(s)
    s_no_duplicated.remove(max(s_no_duplicated))
    print(max(s_no_duplicated))
else:
    print(None)
    
