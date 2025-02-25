# Find whether a number is prime or not

n = 11

for i in range(2, n):
    if(n%i) ==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
    


