class Phone:
    dept="CSE"
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def display(self):
        print("Name ; ",self.name)
        print("Age : ",self.age)
        print("Dept : ",self.dept)


ob1=Phone("Ram",20)
ob1.display()

print()


ob2=Phone("Kumar",21)
ob2.display()

print()


ob3=Phone("Lalit",22)
ob3.display()

print()


ob4=Phone("Kumar",23)
ob4.display()

print()

print("Above are all instances because self=>instances,it change regarding object,\nExcept dept this class variable => not changed")
print()
