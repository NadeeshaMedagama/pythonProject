import time
import random
import os
import test as t
from car import Car

print("Hello World")
print("Hi")


#In python when we use a range first element for start num, sec ele for last num, third ele for jumping num
for i in range(1,10,2):
    print(i)

print("\n")

car1 = Car("Toyota", "BMW", 2023, "Black")
car2 = Car("Ford", "Mustang", 2023, "Yellow")

print(car1.type)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()

print("\n")

print(car2.type)
print(car2.model)
print(car2.year)
print(car2.color)

car2.drive()
car2.stop()
