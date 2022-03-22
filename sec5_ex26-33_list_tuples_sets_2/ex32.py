# https://www.w3schools.com/python/python_lists_comprehension.asp
# Syntax: newlist = [expression for item in iterable if condition == True]
# Ex:     newlist = [x for x in range(10) if x < 5] 

s = [[1,2,3],[4,5,6],[7,8,9]]
# s = [1,2,3,4,5,6,[7,8,9]]
# s = [["a","b","c"],["d","e","f"],["g","h","i"]]
# s = [[],["a0",[1,2,[5]]]]
output = []

s_list_output = []
def flatten(s_list):    
    for x in s_list:
        if type(x) != list: # or isinstance(x, list) # https://docs.python.org/3/library/functions.html#isinstance
            s_list_output.append(x)
        else:
            flatten(x)
    return s_list_output

if s:
    output = flatten(s)
    print("output: ", output)
else:
    print(s)
