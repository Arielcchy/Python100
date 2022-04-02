# Add a Key-Value Pair Only if the Key is Not in the Dictionary

d = {"January": 45, "February": 56, "March": 67}
new_key = "April"
new_value = 67

if new_key not in d.keys():
    d.update({new_key: new_value})
    # or  d[new_key] = new_value
print(d)