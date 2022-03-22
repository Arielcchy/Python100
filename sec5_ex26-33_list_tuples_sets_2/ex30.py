s = [4,5,3,1]

# # Option 1 - set(), remove(min)
# if len(s) > 1:
#     s_no_duplicated = set(s)
#     s_no_duplicated.remove(min(s_no_duplicated))
#     print(min(s_no_duplicated))
# else:
#     print(None)

# Option 2 - sorted(), get the output from designated index
if len(s) > 1:
    s_reversed_sort = sorted(s, reverse=True)
    print(s_reversed_sort[-2])
else:
    print(None)