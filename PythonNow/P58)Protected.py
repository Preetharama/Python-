class Company():
    def display(self):
        self._name="Ram"

class A(Company):
    pass

ob1=A()
ob1.display()
print(ob1._name)

