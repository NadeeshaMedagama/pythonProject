import time
import random
import os
import test
import test as t
from car import Car

temp = int(input("Enter a temperature: \n"))
if(temp >=30 and temp <=45):
    print("Today is a very hot day!")
elif(temp >=0 and temp <=30):
    print("You can goto outside")
elif(temp >45):
    print("You can't goto outside")
else:
    print("You will be a Ice!")

name = ""
while len(name) == 0:
    name = input("\nWhat is your name?")
#print("Hello",name)
print("Hello "+name)

age = int(input("Enter your age: "))
if(age <= 0):
    print("You are not born yet!")
elif(age < 13):
    print("You are a Child")
elif(age >= 18):
    print("You are a Adult")
elif(age >= 13):
    print("You are a Teenager")
else:
    print("You are not born yet!")

for j in "Nadeesha Medagama":
    print(j)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

row = int(input("Enter a number for Rows: "))
col = int(input("Enter a number for Columns: "))
sym = input("Enter a Symbol: ")

for i in range(row):
    for j in range(col):
        print(sym, end=" ")
    print()

phone = "123-456-789-0"

for i in phone:
    if i == "-":
        continue
    print(i, end=" ")
    # print(i)
print("\n")
for j in range(10):
    if j == 3:
        pass
    else:
        print(j, end="")

food = ["orange", "apple", "banana", "strawberry"]
food.append("cake")
food.insert(1, "mango")
for i in food:
    print(i)

student = ("Nadeesha", 22, "male")
print(student.count("Nadeesha"))
print(student.index(22))

for i in student:
    print(i, end=' ')
print("\n")
if "Nadeesha" in student:
    print("Nadeesha is here!")

veg = {"carrot", "coconut", "leaks", "beet"}
fruit = {"banana", "orange", "apple", "grapes", "beet"}
veg.add("cake")
# fruit.update(veg)
veg.update(fruit)
for i in veg:
    print(i, end=" ")
print("\n")
print(veg.difference(fruit))
# print("\n")
print(fruit.intersection(veg))

capitals = {'USA':'Washinton',
            'India':'New Delhi',
            'SL':'Kootte',
            'Jpn':'Tokyo'
            }
print(capitals['USA'])
print(capitals.get('UK'))
print(capitals.values())
print(capitals.keys())
print("\n")
capitals.update({'UK':'London'})
for key, value in capitals.items():
    print(key,"-", value)

print(capitals.values())

name = "Nadeesha Medagama!"
first_name = name[0:8].upper()
second_name = name[9:].lower()
funky_name = name[-1]

print(first_name)
print(second_name)
print(funky_name)

name = "nadeesha"
if(name[0].islower()):
    #name = name.capitalize()
    name = name.upper()
print(name)

def hello(Name, age, village):
    print("Hello World!",Name)
    # print("You are %d years old" %age)
    print("You are", str(age), "years old.")
    print("You live in", village)

myName = "Medagama"
hello(myName, 21 , "Bandaragama")

def multiply(num1, num2):
    result = num1 * num2
    return result

x = multiply(2,4)
print(x)


def hi(first, second, third):
    print("Your name is", first, second, third)

hi(first="Nadeesha", second="Madhubhan", third="Medagama")

#This is Nested function
print(round(abs(float(input("Enter your number: ")))))

name= "Medagama"        #Global scope
def display():
    name = "Nadeesha"       #Local scope
    print(name)
display()
print(name)

def Sum(*args):
    sum = 0
    args = list(args)
    args[2] = 0
    for i in args:
        sum += i
    #print(sum)
    return sum
# Sum(1, 2, 4)
print(Sum(1, 2, 4))

def fullName(**kwargs):         #Parameter that pass all arguments in Dictionary(**__)
    print("Hello", end =" ")
    for key, value in kwargs.items():
        print(value, end = " ")

fullName(title = "Mr.", first = "Nadeesha", second = "Madhubhan", third = "Medagama")

item = "pen"
animal = "cat"

print("The {} is on the {}".format(animal, item))
print("The {animal1} is eating {fruit}".format(animal1 = "dog", fruit = "orange"))
anima1 = "cow"
print(anima1)

text = "My name is {} and I am {} years old."
print(text.format("Nadeesha", 22))

name = "Nadeesha"
print("Your name is {}".format(name))

num = 3.14597
print("Pi number is {:.2f}".format(num))
num = 1000
print("Number is {:,}".format(num))
print("Number is {:b}".format(num))
print("Number is {:o}".format(num))
print("Number is {:X}".format(num))
print("Number is {:E}".format(num))     #This is for scientific number

x = random.randint(1, 5)
print(x)
y = ["paper", "scissor", "rock"]
random.shuffle(y)
print(y)
z = ["orange", "banana", "grapes"]
list = random.choice(z)
print(list)

try:
    num = int(input("Enter a Number: "))
    div = int(input("Enter a Number for Division: "))
    result = num / div

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by Zero!")
except ValueError as e:
    print(e)
    print("Enter Numbers only!")
except Exception as e:
    print(e)
    print("Invalid input for Division!")
else:
    print(result)
finally:
    print("This is always Execution...")

path = "C:\\Users\\MEDAGAMA\\OneDrive - University of Kelaniya\Desktop\\New Text Document.txt"
if (os.path.exists(path)):
    print("Path is Exists")
    if os.path.isdir(path):
        print("Directory Exists")
    elif os.path.isfile(path):
        print("File Exists")
else:
    print("Path is not Exists")

try:
    with open("C:\\Users\\MEDAGAMA\OneDrive - University of Kelaniya\\Desktop\\New Text Documen.txt") as file:
        print(file.read())
#print(file.closed)
except FileNotFoundError as e:
    print(e)
    print("File Not Found")

text = "\nThis is a text.txt"
# with open("test.txt", "w") as file:
#     file.write(text)
#     print("File created successfully!")
with open("test.txt", "a") as file:
    file.write(text)
    print("File updated successfully!")

source = "Folder"
path = "C:\\Users\\MEDAGAMA\OneDrive - University of Kelaniya\\Desktop\\Folder"

try:
    if os.path.exists(path):
        print("There is a file already exists")
    else:
        os.replace(source, path)
        print(source, "was moved")
except FileExistsError as e:
    print(e)

# t.hi()
# t.hello()
from test import hi,hello
hi()
hello()

help("modules")

car1 = Car("Toyota", "BMW", 2023, "Black")
car2 = Car("Ford", "Mustang", 2023, "Yellow")
car3 = Car("Ferrari", "Gollorado", 2024, "White")

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

print("\n")

print(car3.type)
print(car3.model)
print(car3.year)
print(car3.color)

car3.drive()
car3.stop()

car1 = Car()
car2 = Car()
car1.wheels = 6

print(car1.wheels)
print(car2.wheels)

class Animal1:

    alive = True
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal is eating")

class Animal2:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name, "is sleeping")
        return self

    def eat(self):
        print(self.name, "is eating")
        return self

    def walk(self):
        print(self.name, "is walking")
        return self

    def fly(self):
        print(self.name, "is flying")
        return self

class cat(Animal1):

    def walk(self):
        print("Cat is walking")

    def eat(self):
        print("Eating")

class fish(Animal2):

    def swim(self):
        print("Fish is swimming")

class parrot(Animal1, Animal2):

    def fly(self):
        print("Cat is flying")

Cat = cat()
Fish = fish("Fish")
Parrot = parrot("Parrot")

print("Cat is alive:", Cat.alive)

Cat.eat()
Fish.sleep()

Parrot.eat()
Parrot.sleep()

animal2 = Animal2("Monster")
animal2.fly()\
    .sleep()\
    .eat()\
    .walk()

