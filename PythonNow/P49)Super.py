class A:
    def __init__(self):
        print("HI A B=> without constructor")
    def display(self):
        print("Display A")

class B(A):
    def display(self):
        print("Display B")

ob1=B()

class C:
    def __init__(self):
        print("HI C")
    def display(self):
        print("Display C")

class D(C):
    def __init__(self):
        print("HI C with Construor")
    def display(self):
        print("Display D")

ob2=D()

print()
print("I need parent constructor even through I have (child) constructor ==> \"Super Keyword \" ")
print()

class E:
    def __init__(self):
        print("HI E")
    def display(self):
        print("Display E")

class F(E):
    def __init__(self):
        super().__init__()
        print("HI F with Construor")
    def display(self):
        print("Display F")

ob3=F()

