s = "Coding"

# Option 1
# if len(s) > 1:
#     output = s[1::2]
#     print(output)
# else:
#     print(s)

# Option 2
new_s = ""
for i in range(1, len(s), 2): # range(start, stop, step)
    new_s += s[i]
print(new_s)