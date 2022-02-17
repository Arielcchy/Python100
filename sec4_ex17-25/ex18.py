s = [3, 4, 5, 6]

# Option 1 - .join() .rstring()
string_s = ""
string_s += " ".join(str(i) for i in s)
string_s = string_s.rstrip()
print(string_s)

# Option 2 - print()
for i in s:
    print(i, end=" ")

# Option 3 - unpack
print(*s, sep=" ")
