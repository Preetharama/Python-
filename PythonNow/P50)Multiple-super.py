class A:
    def __init__(self):
        print("HI A ")
    def display(self):
        print("Display A")

class B:
    def __init__(self):
        print("HI B")
    def display(self):
        print("Display B")

class C(A,B):
    print(" C(A,B)")
    def __init__(self):
        super().__init__()
        print("HI C")
    def display(self):
        print("Display C")

ob1=C()
print()

class D(B,A):
    print(" D(B,A)")
    def __init__(self):
        super().__init__()
        print("HI D")
    def display(self):
        print("Display D")

ob2=D()
