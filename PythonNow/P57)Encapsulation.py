class Company1():
    def __init__(self):
        self.cname1="Google 1"

    def display(self):
        print(self.cname1)

ob1=Company1()
ob1.display()

print()

class Company2():
    def __init__(self):
        self.___cname2="Google 2"

    def display(self):
        print(self.___cname2)

ob2=Company2()
ob2.display()

print()

""" ERROr => Private only access by within class of methods"""

print()

class Company3():
    def __init__(self):
        self._cname3="Google 3"

class display(Company3):
    def display(self):
        print(self._cname3)

ob3=display()
ob3.display()

print(ob3._cname3)
""" ERROr => Protected access only by child class """

print()




