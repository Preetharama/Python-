class Laptop:
    dept="CSE"

    def __init__(self,a,b):
        self.name=a;
        self.age=b;

    def display(self):
        print(self.name)
        print(self.age)
        print(self.dept)

    def changedept(self,c):
        print(self.name)
        print(self.age)
        self.dept=c
        print(self.dept)

    @classmethod
    def changedeptusingdecalarate(cls,c):
        cls.dept=c
        print(cls.dept)
        
    @staticmethod
    def staticmethod():
        print("Printing static")

ob1=Laptop("RAm",20)
ob1.display()

print()

ob2=Laptop("Lalit",21)
ob2.display()

print()

ob3=Laptop("Ram Kummar",22)
ob3.display()

print()

ob4=Laptop("Lalit Kummar",24)
ob4.changedept("ECE")

print()

Laptop.changedeptusingdecalarate("IT")

print()

Laptop.staticmethod()
