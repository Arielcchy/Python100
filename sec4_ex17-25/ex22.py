s = [1,2,2,3,3,3,4]
elem_to_remove = 2
removed_s = []

# # Option 1
# if len(s) == 0:
#     print("Empty List")
# elif elem_to_remove not in s: 
#     print("Not Found")
# else:
#     for i in s:
#         if elem_to_remove == i:
#             pass
#         else:
#             removed_s.append(i)
#     print(removed_s)

# Option 2 - count(), remove(), mutated original list
if not s:
    print("Empty List")
elif s.count(elem_to_remove) == 0:
    print("Not Found")
else:
    for i in range(s.count(elem_to_remove)):
        s.remove(elem_to_remove)

print(s)
   


