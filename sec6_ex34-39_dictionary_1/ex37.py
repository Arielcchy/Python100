# Check if All Values are Equal

s = {"a":4, "b":4, "c":4}
# s = {}

# # Option 1 - values to a list, compare
# s_list = []
# if len(s) == 0:
#     output = "Empty"
# else:
#     s_list.extend(s.values())
#     for i in range(len(s_list)-1):
#         if s_list[i] == s_list[i+1]:
#             output = True
#         else:
#             output = False
#             break
# print(output)

# Option 2 - values to a set: remove all the duplicates    
no_duplicate_values = set(s.values())    

if len(no_duplicate_values) == 0:
    print("Empty")
elif len(no_duplicate_values) == 1:
    print(True)
else:
    print(False)


