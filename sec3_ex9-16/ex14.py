import re

s = "Hello World yO"
# # Option 1
# separate_indices = [z for z, x in enumerate(s) if x == " "]
# # https://book.pythontips.com/en/latest/enumerate.html
# # https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
# # https://realpython.com/python-enumerate/

# list_s = s.split(" ")
# def printString(input):
#     output_s = input + " " 
#     reverse_s = reversed(output_s)
    
#     for i in reverse_s:
#         print(i)
        
# for j in list_s:
#     output_s = ""
#     for cha in j:
#         if re.search("[a-z]",cha): # isupper() islower() -> boolean
#             cha_cased = cha.upper()   
#         else:
#             cha_cased = cha.lower()
#         output_s += cha_cased

#     printString(output_s)

# Option 2
new_s = ""
words_list = s.split(" ")

for word in words_list:
    reversed_word = "".join(reversed(word))
    swapped_cased = reversed_word.swapcase()
    new_s += swapped_cased + " "

new_s.rstrip()
print(new_s)
        
        
        





