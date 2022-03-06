s = "Wonderful"

# if len(s) >= 6:
#     last3_front3 = s[:3]+s[(len(s)-3):]
#     print(last3_front3)
# else:
#     print("")

# optimization
num_chars = 3
if len(s) >= num_chars*2:
    last3_front3 = s[:num_chars]+s[(len(s)-num_chars):]
    print(last3_front3)
else:
    print("")