pointA = [-3,4,-5]
pointB = [2,0,-4]
addition = 0 # "sum" is a build-in word in python
addition_math = 0
# Option 1
for a, b in zip(pointA, pointB):
    addition += (a-b)**2

print(addition**0.5)

# Option 2 - math module
import math

for a, b in zip(pointA, pointB):
    addition_math += (a-b)**2

print(math.sqrt(addition_math))
