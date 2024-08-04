class Dad:
    def phone(self):
        print("Parent dad")

class Son(Dad):
    def laptop(self):
        print("Child laptop")

ob1=Dad()
ob2=Son()

ob1.phone()
ob2.laptop()

ob2.phone()
