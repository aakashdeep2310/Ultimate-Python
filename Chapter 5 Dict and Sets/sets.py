
s = set() #create empty set
print(s)
# create a set
s1 = {1,2,3,4,5,5,5,5,5,5,5} #elements can't be repeated in set and order is not maintained
print(s1)   

#set is a collection of well defined objects or elements
#set is mutable
#set contains only unique elements and can not have duplicate elements

#sets are unindexed and unordered


#methods of set
s1.add(6) # add element in set
s1.add(3) # add element in set
s1.add(4) # add element in set
s1.add(2) # add element in set
s1.add(7) # add element in set

s1.remove(3) # remove element from set
s1.discard(3) # remove element from set if available
s1.clear() # clear the set
s11 = s1.copy() # copy the set
print(s11)
print(s1)

set1 = {1,2,3,4,5, "Aakash Deep Singh"}
print(set1)
print(type(set1))