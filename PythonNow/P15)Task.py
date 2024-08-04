a=int(input("a="))
b=int(input("b="))

"""
Print number between a and b """

print("Print number between a and b")

for ele in range(a+1,b+1):
    print(ele)

print("..................................")
"""
Print even number of a to b """

print("Print even number of a to b")
for ele in range(a,b+1):
    if(ele%2==0):
        print(ele)

print("..................................")


"""
Count odd numbers in 1 to 10"""

print("Count odd numbers in 1 to 10")
c=0
for ele in range(a,b+1):
    if(ele%2!=0):
        c+=1;
print(c)
print("..................................")


"""
Count numbers of even & odd numbers in 1 to 10"""
e_c=0
o_c=0
for ele in range(a,b+1):
    if(ele%2==0):
        e_c+=1
    else:
        o_c+=1
print("Even count => ",e_c,"Odd Count => ",o_c)
