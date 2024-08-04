class Granddad:
    def phone(self):
        print("Grand Parent")

class Dad(Granddad):
    def food(self):
        print("Parent dad")

class Son(Dad):
    def laptop(self):
        print("Child laptop")

ob1=Son()

ob1.phone()
ob1.food()
ob1.laptop()
