# print star pattern

'''
  *
 ***
*****


'''

num = 5

for i in range (1, num+1):
    print(" "*(num-i), end = "")
    print("*" * (2*i-1), end = "")
    print("")
    