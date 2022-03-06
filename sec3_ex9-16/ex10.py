# s = ["Hello","The quick brown fox jumps over the lazy dog", "abcdefghijklmnopqrstuvwxyz"]
s = "The quick brown fox jumps over the lazy dog"

# Option 1
# allAlphabet = "abcdefghijklmnopqrstuvwxyz"
# allAlphabet_list = [" "]
# for bench_mark in allAlphabet:
#     allAlphabet_list.append(bench_mark)

# lower_case = str.lower(s)
# if len(s) >= len(allAlphabet):
#     for lower_char in lower_case:
#         if lower_char in allAlphabet_list:
#             continue
#         else:
#             print("False")
#             break
#     print("True")
# else:
#     print("False")

# # Option 2
# import string
# set_s = set(s.lower())

# if " " in set_s: # if don't check space existence, it will throw an error if there is none
#     set_s.remove(" ")
# print(set_s == set(string.ascii_lowercase))

# Option 3
import string

is_pangram = True
for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break

print(is_pangram)
