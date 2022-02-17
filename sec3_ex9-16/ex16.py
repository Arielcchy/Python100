# 38. Sort Words in Alphabetical Order
s = "Hello World"

# # Option 1 - split(), join(), sorted()
# s_lower = s.lower()
# s_lower_list = s_lower.split(" ")
# output = ""
# for singleString in s_lower_list:
#     s_sorted = "".join(sorted(singleString))
#     output += s_sorted + " "

# output.rstrip()
# print(output)

# Option 2 - compacted sorted() and lower()

new_s = ""
word_list = s.split()

for word in word_list:
    new_s += "".join(sorted(word.lower())) + " "

new_s = new_s.rstrip()

print(new_s)