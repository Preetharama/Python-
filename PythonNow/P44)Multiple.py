class Dad:
    def phone(self):
        print("Parent dad")

class Mom:
    def food(self):
        print("Parent mom")

class Son(Dad,Mom):
    def laptop(self):
        print("Child laptop")

ob1=Son()

ob1.phone()
ob1.food()

