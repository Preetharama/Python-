""" Prepare a mini-calculator """

a=int(input("A : "))
b=int(input("B : "))
print("Addition => Enter add\nSubraction =>  Enter sub\nMultiplcation =>  Enter multi\nDivision =>  Enter div")
operation=input()
if(operation=="add"):
    print("A + B = ",a+b)
elif(operation=="sub"):
    print("A - B = ",a-b)
elif(operation=="multi"):
    print("A * B = ",a*b)
elif(operation=="div"):
    print("A / B = ",a/b)
else:
    print("Invalid inputs => change values")
