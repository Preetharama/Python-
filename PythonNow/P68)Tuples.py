lst =[1,2.4,"Hi",'A']
print(lst)

for i in lst:
    print(i)

lst.insert(0,6)
print(lst)
del lst[2]
print(lst)

lst.append(10)
print(lst)

lst.reverse()
print(lst)

e=lst.count(lst)
print(e)

lst.append(lst)
print(lst)

e=lst.count(lst)
print(e)

l1=[1,2,3,4,0,0.1,7,2.0]
l1.sort()
print(l1)
l1.sort()
l1.reverse()
print(l1)
print(l1[::])
print(l1[::-1])

print(l1[1::-1])


lst2=l1
print(lst2)
