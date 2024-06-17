#printing in python 
print("Hello, World!")

#variables
a = 5
b = 10
print(a + b)

#data types
a = 5
b = 10.5
c = "Hello"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#assign Multiple Values to Multiple Variables
a, b, c = 5, 10.5, "Hello"
print(a)
print(b)
print(c)
#One Value to Multiple Variables
a = b = c = "Orange"
print(a)
print(b)
print(c)
#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#String
a = "Hello, World!"
print(a[1]) #e
print(a[2:5]) #llo
print(a[:5]) #Hello
print(a[2:]) #llo, World!
print(a[-5:-2]) #orl

#Operators
a = 5
b = 10
print(a + b) #15
print(a - b) # -5
print(a * b) # 50
print(a / b) # 0.5
print(a % b) # 5
print(a ** b) # 9765625
print(a // b) # 0

                                                ## Python Arrays ##

#List
fruits = ["apple", "banana", "cherry"]  #list
fruits[1] = "kiwi"  #change value
print(fruits)  # ['apple', 'kiwi', 'cherry']  
#list length
print(len(fruits))  #3
#list append
fruits.append("orange")  #['apple', 'kiwi', 'cherry', 'orange']
#list pop
fruits.pop(1)  #['apple', 'cherry', 'orange']
#list remove
fruits.remove("cherry")  #['apple', 'orange']
#list sort
fruits.sort()  #['apple', 'orange']
#list reverse
fruits.reverse()  #['orange', 'apple']
#list copy
fruits_copy = fruits.copy()  #['orange', 'apple']
#loop through a list
for x in fruits:
  print(x)
#check if item exists
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No, 'apple' is not in the fruits list")
#list join
fruits.extend(["grape", "mango"])  #['orange', 'apple', 'grape', 'mango']
#list insert
fruits.insert(1, "pineapple")  #['orange', 'pineapple', 'apple', 'grape', 'mango']
#list count
fruits.count("apple")  #2
#list index
fruits.index("apple")  #1



#Tuple
fruits = ("apple", "banana", "cherry")  #tuple
fruits[1] = "kiwi"  #tuple is immutable
#tuple length
print(len(fruits))  #3
#tuple append
fruits.append("orange")  #tuple is immutable
#tuple pop
fruits.pop(1)  #tuple is immutable
#tuple remove
fruits.remove("cherry")  #tuple is immutable
#tuple sort
fruits.sort()  #tuple is immutable
#tuple reverse
fruits.reverse()  #tuple is immutable
#tuple copy
fruits_copy = fruits.copy()  #tuple is immutable
#loop through a tuple
for x in fruits:
  print(x)
#check if item exists   
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("No, 'apple' is not in the fruits tuple")
#tuple join
fruits.extend(["grape", "mango"])  #tuple is immutable
#tuple insert
fruits.insert(1, "pineapple")  #tuple is immutable
#tuple count
fruits.count("apple")  #2
#tuple index
fruits.index("apple")  #1

#Set
fruits = {"apple", "banana", "cherry"}  #set
fruits.add("orange")  #add item
fruits.remove("banana")  #remove item
fruits.clear()  #clear set
#check if item exists
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits set")
else:
  print("No, 'apple' is not in the fruits set")
#set copy
fruits_copy = fruits.copy()  #set is immutable
#loop through a set
for x in fruits:
  print(x)
#set join
fruits.update(["grape", "mango"])  #set is immutable
#set discard
fruits.discard("banana")  #set is immutable
#set pop
fruits.pop()  #set is immutable
#set copy
fruits_copy = fruits.copy()  #set is immutable
#set length
print(len(fruits))  #3

#Dictionary
fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}  #dictionary
fruits["apple"] = "green"  #change value
fruits.pop("banana")  #remove item
fruits.clear()  #clear dictionary
#check if item exists
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits dictionary")
else:
  print("No, 'apple' is not in the fruits dictionary")
#dictionary copy
fruits_copy = fruits.copy()  #dictionary is immutable
#loop through a dictionary
for x in fruits:
  print(x)
#dictionary join
fruits.update({"grape": "green", "mango": "yellow"})  #dictionary is immutable
#dictionary length
print(len(fruits))  #3
#dictionary items
print(fruits.items())  #dict_items([('apple', 'green'), ('cherry', 'red'), ('grape', 'green'), ('mango', 'yellow')])
#dictionary keys
print(fruits.keys())  #dict_keys(['apple', 'cherry', 'grape', 'mango'])
#dictionary values
print(fruits.values())  #dict_values(['green', 'red', 'green', 'yellow'])
    
                                                    ## Python Conditions and If statements 
#If statement
a = 5
b = 10 
if a > b:
  print("a is greater than b")
elif a == b:
  print("a is equal to b")
else:
  print("a is less than b")
#Nested if statement
a = 5
b = 10
if a > b:
  print("a is greater than b")
else:
  if a == b:
    print("a is equal to b")
  else:
    print("a is less than b")
#Else statement
a = 5
b = 10
if a > b:
  print("a is greater than b")
else:
  print("a is less than b")
#Ternary operator
a = 5
b = 10
print("a is greater than b") if a > b else print("a is less than b")
#Short hand if statement
a = 5
b = 10
c = "a is greater than b" if a > b else "a is less than b"
print(c)
#Short hand if else statement
a = 5
b = 10
c = "a is greater than b" if a > b else "a is less than b"
print(c)

                                       ##loops##

#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#While loop
i = 0
while i < 5:
  print(i)
  i += 1
#Break statement
i = 0
while i < 5:
  print(i)
  if i == 2:
    break
  i += 1
#Continue statement
i = 0
while i < 5:
  i += 1
  if i == 2:
    continue
  print(i)
#Else statement
i = 0
while i < 5:
  print(i)
  i += 1
else:
  print("i is no longer less than 5")
#Range function
for x in range(5):
  print(x)
#Range function with start and stop
for x in range(2, 5):
  print(x)
#Range function with start, stop and step
for x in range(2, 30, 3):
  print(x)

#Nested loops
for x in range(5):
  for y in range(5):
    print(x, y)
#Pass statement
for x in range(5):
  pass
    
                                            ##Functions##

#Defining a function
def my_function():
  print("Hello, World!")
#Calling a function
my_function()
#Defining a function with arguments
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Defining a function with default value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#Defining a function with return value
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#Defining a function with multiple arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
my_function("Tobias", "Refsnes")
my_function("Linus", "Refsnes")
#Defining a function with variable number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#Defining a function with variable number of keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#Defining a function with lambda
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#Defining a function with nested functions
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))

                                               ##Classes and Objects##

#Creating a class
class MyClass:
  x = 5
#Creating an object
p1 = MyClass()
print(p1.x)
#Creating a class with method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#Creating a class with method and object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
#Creating a class with method and object with arguments
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
#Creating a class with inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
#Creating a class with inheritance and method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#Creating a class with inheritance and method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()

                                                ##inputs and outputs##

#Input
name = input("Enter your name: ")
print("Hello, " + name)
#Output
print("Hello, World!")


##Resources
#https://www.w3schools.com/python/default.asp