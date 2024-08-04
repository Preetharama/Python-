class Animal():
    def sound(self):
        print(" Animal makes a sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog makes a sound")

class Bird(Animal):
    def sound(self):
        print("Birds makes a sound")

ob1=Bird()
ob2=Dog()
ob3=Animal()
ob1.sound()
ob2.sound()
ob3.sound()
