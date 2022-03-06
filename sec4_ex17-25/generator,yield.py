# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

# Iteration - use []
mylist = [x*x for x in range(3)]
for a in mylist:
    print("a = ", a)
for b in mylist:
    print("b = ", b)
# Iteration can perform for i in mygenerator a second time since iteration stores all the values in memory.


# Generator - use ()
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print("i = ", i)
for j in mygenerator:
    print("j = ", j)
# Generator cannot perform for i in mygenerator a second time since generators can only be used once.

# Yield
# a keyword that is used like return, except the function will return a generator