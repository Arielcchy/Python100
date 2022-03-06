# Option 1: Slicing (more common)
s = "Hello"
reverse = s[::-1] 
# print(reverse)

# string[start:stop:step]
# string[::step] means start and stop are default value


# Option 2: build in function
reversed_word = "".join(reversed(s))
print(reversed_word)
# for i in reversed(s): # if it's just reversed(string)
#     print(i)