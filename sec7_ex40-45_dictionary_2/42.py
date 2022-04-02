# Print the Max Sum of Values
my_dict = {
    "a": [1, 2, 3],
    "b": [45, 12, 100],
    "c": [3, 5, 9],
   	"d": [4, 0, -4]
}
output = 0
for my_list in my_dict.values():
    if sum(my_list) > output:
        output = sum(my_list)
print(output)

# Python - List Comprehension
# https://www.w3schools.com/python/python_lists_comprehension.asp
# List comprehension offers a shorter syntax when you want to "create a new list" based on the values of an existing list
# output = [sum(my_list) for my_list in my_dict.values() if sum(my_list) > output]
