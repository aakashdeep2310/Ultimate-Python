#tuple is immutable
t = (1, 2, 3, 4, 5)
t1 = () #Empty tuple


print(t)
print(type(t))
print(type(t1))

t2 = (1) # this is type int class not a tuple
t3 = (1,) # this is type tuple class, comma is necessary to make it a tuple

#mix type of element in tuple
a = (1, 2.5, "Hello", True)
print(a)

# a[0] = 5    #This will give an error as tuple is immutable
