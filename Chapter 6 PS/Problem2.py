math = int(input("Enter your math score: "))
phy = int(input("Enter your physics score: "))
chem = int(input("Enter your chemistry score: "))

avg = (math + phy + chem) / 3

if(avg >= 40 and math >= 33 and phy >= 33 and chem >= 33):
    print("You have passed the exam")
else:
    print("You have failed the exam")