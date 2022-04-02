# Sort Lists in Ascending Order 
my_dict = {
    "a": [4, 3, 2],
    "b": [5, 3, 7],
    "c": [1, 9, 10],
   	"d": [3, 4, 1]
}

for k, v_list in my_dict.items():
    # my_dict[k] = sorted(v_list) # sorted() returns a sorted "copy" of the list (not a mutated list)
    v_list.sort() # .sort() sorts a list (the list is mutated/changed, store in the "memory")

print(my_dict)