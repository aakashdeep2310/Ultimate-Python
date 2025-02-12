name = "Aakash"

negativeSlicedString = name[-5:-1] # left side index is inclusive but right side index is exclusive
slicedString = name[1:5] # right side index is exclusive

print(negativeSlicedString)
print(slicedString)

print(name[-1]) # prints the last character of the string
print(name[0]) # prints the first character of the string
print(name[:5]) # prints the first 5 characters of the string
print(name[1:]) # prints the string from the second character to the end