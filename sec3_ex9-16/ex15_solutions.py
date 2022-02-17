# 36. Count Repeated Characters 
s = "Corporation"

# repeated_chars_count = 0
# repeated_chars = []

# # find how many chars have shown more than one time in a string
# for char in s:
#     if (s.count(char) > 1) and (char not in repeated_chars):
#         repeated_chars_count += 1
#         repeated_chars.append(char)
# print(repeated_chars_count)

# print repeated_chars list in a sorted order, in the same line
# Option 1
# if repeated_chars:
#     for char in sorted(repeated_chars):
#         print(char, end="@")
# else:
#     print(None)

# Option 2 - prevent looping
# if repeated_chars:
#     print(*sorted(repeated_chars), sep="@") # * is an unpack operator for list and tuple; ** is for dictionary
#     # https://geekflare.com/python-unpacking-operators/
# else:
#     print(None)   

# Option 3 - remove count, use len() to count, unpack asterisk
repeated_chars = []

for char in s:
    if (s.count(char) > 1) and (char not in repeated_chars):
        repeated_chars.append(char)
print(len(repeated_chars))

if repeated_chars:
    print(*sorted(repeated_chars), sep="@") # * is an unpack operator for list and tuple; ** is for dictionary
    # https://geekflare.com/python-unpacking-operators/
else:
    print(None)  