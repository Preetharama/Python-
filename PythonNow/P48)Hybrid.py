class Dad:
    print("Dad property ")

class Property:
    print("Hybrid ")

class Son1(Dad,Property):
    print("Son1 property ")

class Son2(Dad):
    print("Son2 property")

class Son3(Dad):
    print("Son3 property")

ob=Son3()


    
