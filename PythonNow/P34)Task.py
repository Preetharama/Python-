"""
Class name Laptop
create different object and pass different values
"""
class Laptop:
    price=100000
    processor=2.5
    ram=24
ob=Laptop()
HP=Laptop()
dell=Laptop()

print("Normal Object ")
print("Price",ob.price)
print("Processor",ob.processor)
print("Ram",ob.ram)
print()

HP.price=20000
HP.processor=3.5
HP.ram=34
print("HP Object ")
print("Price",HP.price)
print("Processor",HP.processor)
print("Ram",HP.ram)
print()

dell.price=30000
dell.processor=4.5
dell.ram=64
print("Dell Object ")
print("Price",dell.price)
print("Processor",dell.processor)
print("Ram",dell.ram)
print()
