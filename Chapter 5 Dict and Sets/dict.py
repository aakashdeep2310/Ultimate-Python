# dictionary is mutable 

# create a dictionary

d ={} #empty dictionary
d1 = {1} # dictionary with one element
d2 = {1,2,3,4} # dictionary with multiple elements
d3 = {1: 'value', 'key': 2} # dictionary with key value pair
d4 = dict({1: 'value', 'key': 2}) # using dict() constructor
d5 = dict([(1, 'value'), ('key', 2)]) # creating dictionary with list of tuples
# print(d1)

dict = {
    "Aakash" : 1,
    "Aman" : 2,
    "Aaditya" : 3,
    "Aarav" : 4,
    "Sumit" : 5
}

# print(dict)

# dict.update({"Amit" : 6})
# print(dict)
# dict.clear()
# print(dict)

#methods of dictionary

# print(dict.get("Aakash1")) # get the value of key if available otherwise return None
# print(dict['Aakash1']) # get the value of key if available otherwise throw an error
# print(dict.items())
