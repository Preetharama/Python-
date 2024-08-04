class Shape():
    def area(self):
        return "WE"
        

class Rectangle(Shape):
    def area(self):
        a=10
        b=10
        print(a*b)

ob1=Shape()
print(ob1.area())

ob2=Rectangle()
print(ob2.area())
