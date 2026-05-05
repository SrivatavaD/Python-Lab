# Basic Concept of OOP in Python
# ------------------------------
# OOP means Object-Oriented Programming.
#
# In OOP, we write code using "classes" and "objects".
#
# Class  = a blueprint or design
# Object = a real thing created from that blueprint
#
# Example:
# Class  = Student
# Object = Aman, Riya, Kabir


print("Basic OOP concepts in Python")


# 1. Creating a simple class
# A class is created using the class keyword.
class Student:
    # __init__ is a special method called a constructor.
    # It runs automatically when we create a new object.
    def __init__(self, name, age, course):
        # self means the current object.
        # These are called attributes or properties.
        self.name = name
        self.age = age
        self.course = course

    # A function inside a class is called a method.
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# 2. Creating objects from the class
# student1 and student2 are objects of the Student class.
student1 = Student("Aman", 21, "Python")
student2 = Student("Riya", 20, "Data Science")


# 3. Calling methods using objects
print("Student 1 details:")
student1.show_details()

print("Student 2 details:")
student2.show_details()


# 4. Accessing object attributes directly
print("Student 1 name:", student1.name)
print("Student 2 course:", student2.course)


# 5. Another simple class example
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def start(self):
        print(self.brand, "car has started.")

    def show_speed(self):
        print("Speed:", self.speed, "km/h")


car1 = Car("Toyota", "White", 80)
car2 = Car("Honda", "Black", 100)

print("Car examples:")
car1.start()
car1.show_speed()

car2.start()
car2.show_speed()


# 6. Constructors in OOP
# A constructor is a special method that runs automatically
# when we create a new object.
#
# In Python, __init__ is used as the constructor.
# It is mainly used to give starting values to an object.
class ConstructorStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


constructor_student1 = ConstructorStudent("Aman", 21)
constructor_student2 = ConstructorStudent("Riya", 20)

print("Constructor example:")
constructor_student1.show_details()
constructor_student2.show_details()


# 7. Without constructor
# Here we create the object first and then add values manually.
class StudentWithoutConstructor:
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


student_without_constructor = StudentWithoutConstructor()
student_without_constructor.name = "Kabir"
student_without_constructor.age = 22

print("Without constructor:")
student_without_constructor.show_details()


# 8. Default constructor
# A default constructor does not take extra values from the user.
# It only has self as a parameter.
class DefaultCar:
    def __init__(self):
        self.brand = "Toyota"
        self.color = "White"

    def show_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


default_car = DefaultCar()

print("Default constructor:")
default_car.show_details()


# 9. Parameterized constructor
# A parameterized constructor takes values from the user.
class ParameterizedCar:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


parameterized_car1 = ParameterizedCar("Honda", "Black")
parameterized_car2 = ParameterizedCar("BMW", "Blue")

print("Parameterized constructor:")
parameterized_car1.show_details()
parameterized_car2.show_details()


# 10. Real-life constructor example
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(self.account_holder, "has balance", self.balance)


account1 = BankAccount("Riya", 5000)
account2 = BankAccount("Aman", 8000)

print("Real-life constructor example:")
account1.show_balance()
account2.show_balance()


# Important OOP words:
# class      = blueprint
# object     = real item created from a class
# attribute  = variable inside an object
# method     = function inside a class
# self       = refers to the current object
# __init__   = constructor that runs when an object is created
# constructor = special method used to give starting values to an object
