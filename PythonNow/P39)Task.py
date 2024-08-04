class Teacher:

    def __init__(self):
        self.name="Ram"
        self.regno="1"
        
    def __init__(self,a,b):
        self.name="Ram"
        self.regno="1"

        self.name=a
        self.regno=b

    def __init__(self):
        self.name="Ram"
        self.regno="1"
        
        
    def display(self):
        print(self.name)
        print(self.regno)

ob=Teacher()
ob.display()

