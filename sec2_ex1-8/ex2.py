s = ["Pizza","H","Hello","Amazing"]
i = 4
# for word in s: 
#     try: 
#         if word[i]:
#             print(word[i])
#         elif len(word)==0 :
#             print("Empty String")
#     except:
#         print("i is out of range")

for word in s:
    if not word: # Truesy, Falsy: python build in for empty judgement
        print("Empty String")
    elif i<len(word):
        print(word[i])
    else:
        print("i is out of range")