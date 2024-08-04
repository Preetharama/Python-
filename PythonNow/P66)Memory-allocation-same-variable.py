a=20
b=20
print(" a=20 b=20 a and b address are ")
print(id(a))
print(id(b))
print("Now b's value is changed to 10")
b=10
print(id(b))
print()

c=1
d=c
print(" c=1 d=c c and d address are ")
print(id(c))
print(id(d))
print("Now d's value is changed to 10")
d=10
print(id(d))
