class Animal():
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog makes a sound.")

class Birds(Animal):
    def sound(self):
        print("Birds makes a sound.")


ob1=Animal()
ob1.sound()

ob1=Dog()
ob1.sound()
    
ob2=Birds()
ob2.sound()
    
