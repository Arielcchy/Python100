s = "Hello"
Suffix = "ello"

# # Option 1 - build-in
# print(s.endswith(Suffix))

# Option 2 - slice
print(s[-len(Suffix):] == Suffix)
