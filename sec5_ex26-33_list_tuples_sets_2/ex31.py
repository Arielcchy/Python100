# s = [1,2,3,4,3,2,1,2]
s = ["a","a","b","c","A","b"]
s_dic = {}
for x in s:
    if x in s_dic.keys():
        s_dic[x] += 1
    else:
        s_dic[x] = 1

print(s_dic)