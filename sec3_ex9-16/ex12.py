s = "Coding"
Prefix = "Cod"

# # Option 1
# match_prefix = True

# if len(Prefix) > len(s):
#     match_prefix = False
# else:
#     for i in range(0,len(Prefix)):
#         if s[i] != Prefix[i] :
#             match_prefix = False
#             break
# print(match_prefix)

# # Option 2
# # https://www.w3schools.com/python/python_regex.asp
# import re
# x = re.search(f"^{Prefix}",s)
# if x:
#     print("True")
# else:
#     print("False")

# # Option 3 - slice
# print(s[:len(Prefix)] == Prefix)

# Option 4 - build-in
print(s.startswith(Prefix))



