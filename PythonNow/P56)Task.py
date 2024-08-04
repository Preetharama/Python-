class Employee():
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):

    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept

    def display(self):
        print(self.name,self.salary,self.dept)

ob1=Manager("RAM",2000,"CSE")
ob1.display()
