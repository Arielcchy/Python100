listA = []
listB = [1,2,3,4]

# Option 1 - convert to set(), use set.difference()
setA = set(listA)
setB = set(listB)
print(set.difference(setA, setB))

# Option 2 - for loop
output = []
for a in listA:
    if a not in listB:
        output.append(a)
print(output)
