s = ["Hello","35677", "Hello234", ""]

for i in s:
    if i.isdigit(): # or i.isdecimal()
        print("True")
    else:
        print("False")