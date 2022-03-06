s = ["Hello","Worldipq", "Dog", ""]
n = 6

# Option 1: Slicing
# for i in s:
#     output = i[:n] + i[n+1:]
#     print(output)

# Option 2: Generator Expression
for i in s:
    output = ""
    for x in range(len(i)):
        if x != n:
            output += i[x]
        else:
            continue
    # This for loop is equivalent to:
    # output = ''.join(i[x] for x in range(len(s)) if x != i)
    print(output)