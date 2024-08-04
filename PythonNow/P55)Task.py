class Person():
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def display(self):
        print(self.name)
        print(self.grade)

ob1=Student("Ram","A")
ob1.display()
