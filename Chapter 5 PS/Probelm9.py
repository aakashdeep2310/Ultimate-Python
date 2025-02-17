s = {8, 7, 12, "Aakash", [1,2]}

# print(s) # TypeError: unhashable type: 'list'
s.update([1,2,3,4])
print(s) # {1, 2, 3, 4, 7, 8, 12, 'Aakash'}

# print(s[0]) # TypeError: 'set' object is not subscriptable