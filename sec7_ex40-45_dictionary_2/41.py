# Make a Dictionary from Nested Lists
nested_lists = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
# nested_lists = []
output = {}
# 1. de-nest once : ["a",1] - for loop
for denest in nested_lists:
# 2. use list index to assign them to designated location in a dictionary
    output[denest[0]] = denest[1]

print(output)