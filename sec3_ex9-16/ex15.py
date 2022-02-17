s = "Corporationr"

s_dic = {}
# https://www.w3schools.com/python/python_dictionaries_access.asp
for char in s:
    if char in s_dic:
        s_dic[char] += 1
    else:
        s_dic[char] = 0

max_key = max(s_dic, key=s_dic.get)
# max(d, key = d.get) # which is equivalent to max(d, key = lambda k : d.get(k))
print(max_key)
max_value = max(s_dic.values())
# max(d.items(), key = lambda k : k[1])
print(max_value)


########################
# count_list = []
# alpha_list = []
# start = 0
# for cha in s:
#     start += 1
#     count = 0
#     for i in range(start,len(s)):
#         if s[i] == cha:
#             count += 1
#         else:
#             continue
#     if count != 0:
#         count_list.append(count)
#         alpha_list.append(cha)

# for repeat_count, alphabet in zip(count_list, alpha_list):
#     print(repeat_count, alphabet)

