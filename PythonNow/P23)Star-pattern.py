"""
output
*
**
***
****
*****
"""
for i in range(1,6):
    if(i>1):
        print()
    for j in range(1,i+1):
        print("*",end="")
