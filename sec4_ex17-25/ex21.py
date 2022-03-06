s = [1,2,3]

# # Option 1 - range()
# if s:
#     for i in range(len(s)):
#         print(f"{s[i]} {i}")
# else:
#     print("Empty List")

# Option 2 - Enumerate(): reture a sequence of the list: [(0, ), (1, )] & elements
if s:
    for i, el in enumerate(s):
        print(el, i)
else:
    print("Empty List")
