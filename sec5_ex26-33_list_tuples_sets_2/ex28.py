pointA = [4,5,6]
pointB = [1,2,3]

# # Option 1 - set()
# output = set()
# output = set.intersection(set(pointA), set(pointB))
# print(output)

# Option 2 - violent
output = []
for a in pointA:
    if a in pointB:
        output.append(a)
print(output)
