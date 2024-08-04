"""
Count numbers divide by 3 and 5"""

print("Count numbers divide by 3 and 5")
c=0
for ele in range(1,100+1):
    if(ele%3==0 and ele%5==0):
        c+=1
print(c)
