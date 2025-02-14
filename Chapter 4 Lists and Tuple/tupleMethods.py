a = (1, 45, False, 3.14, "Hello", 45)

print(a)
no = a.count(45) #Counts the number of occurrences of an element in a tuple
print(no)

i = a.index(3.14) #Returns the index of the first occurrence of an element in a tuple
print(i)
print(len(a)) #Returns the length of the tuple
a1 = (1, 2, 3, 4, 5)
print(max(a1)) #Returns the maximum element of the tuple
print(min(a1)) #Returns the minimum element of the tuple
print(sum(a1)) #Returns the sum of all the elements in the tuple


print( 2 in a1) #Returns True if the element is present in the tuple, else False
repeat = a1 * 2 #Repeats the tuple
print(repeat)

print(a1[0:4]) #Slicing a tuple

a2, b2, c2, d2, e2 = a1 #Unpacking a tuple

print(a2, b2, c2, d2, e2)