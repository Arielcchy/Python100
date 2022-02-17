s = ["ab",5]
factor = 2

# # Option 1: naive, create a new list
# new_s = []
# for char in s:
#     new_s.append(char*factor)
# print(new_s)

# # Option 2: use list index, replace list directly
# for i in range(len(s)):
#     s[i] *= factor
# print(s)

# Option 3: enumerate, replace list directly
for i, char in enumerate(s):
    s[i] = char * factor

print(s)