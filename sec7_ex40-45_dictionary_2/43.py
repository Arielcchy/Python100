# Make a Frequency Dictionary for the Characters in a String 
s = "Excellent"
output = {}

# Option 1:
s = ''.join(x.lower() for x in s if x.isalpha())
# Option 2: s = ''.join(filter(str.isalpha, s)
# Option 3: import re 
#           s = re.sub('[^a-zA-Z]','',s)  
#           re.sub(pattern, repl(acement), string, count=0, flags=0)
#           https://docs.python.org/3/library/re.html#re.sub

for l in s.lower(): # for l in s.lower(): if l.isalpha():
    if l in output:
        output[l] += 1
    else:
        output[l] = 1

print(output)