try:

    print("HI")
    printt("HI")
    
    """ Compilertime error """

    a=10
    b=10
    print(a+a)

    """ Logical error => a+b is correct """

    c=int(input("Enter "))
    d=int(input("Enter "))

    """ if d=> value is "aaa"=> enter as string """

except Exception as e:
    print(e)

finally:
    print("THis is Exception")
