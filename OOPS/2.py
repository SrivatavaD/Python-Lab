# More Basic OOP Examples in Python
# ---------------------------------
# This file continues from 1.py.
# It shows a few more common OOP ideas using simple examples.


print("More OOP basic examples in Python")
print("----------------------------------")


# 1. Instance variables and class variables
# Instance variables are different for every object.
# Class variables are shared by all objects of the class.
class Employee:
    company_name = "Tech World"  # class variable

    def __init__(self, name, salary):
        self.name = name          # instance variable
        self.salary = salary      # instance variable

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)


employee1 = Employee("Aman", 30000)
employee2 = Employee("Riya", 35000)

print("\n1. Instance variable and class variable")
employee1.show_details()
employee2.show_details()


# 2. Updating object data using a method
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Not enough balance.")

    def show_balance(self):
        print(self.account_holder, "has balance:", self.balance)


account1 = BankAccount("Kabir", 5000)

print("\n2. Updating object data using methods")
account1.show_balance()
account1.deposit(2000)
account1.withdraw(1000)
account1.show_balance()


# 3. Encapsulation
# Encapsulation means keeping data and methods together inside a class.
# In Python, we commonly use _ before a variable name to show it is internal.
class MobilePhone:
    def __init__(self, brand, battery):
        self.brand = brand
        self._battery = battery

    def charge(self, amount):
        self._battery += amount
        if self._battery > 100:
            self._battery = 100

    def show_battery(self):
        print(self.brand, "battery:", self._battery, "%")


phone1 = MobilePhone("Samsung", 60)

print("\n3. Encapsulation example")
phone1.show_battery()
phone1.charge(30)
phone1.show_battery()


# 4. Inheritance
# Inheritance allows one class to use properties and methods of another class.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking.")


dog1 = Dog("Tommy")

print("\n4. Inheritance example")
dog1.eat()
dog1.bark()


# 5. Method overriding
# Method overriding means child class has a method with the same name
# as the parent class method.
class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a kick.")


class Car(Vehicle):
    def start(self):
        print("Car is starting with a key.")


bike1 = Bike()
car1 = Car()

print("\n5. Method overriding example")
bike1.start()
car1.start()


# 6. Polymorphism
# Polymorphism means same method name can behave differently
# for different objects.
class Circle:
    def area(self):
        print("Area of circle = pi * radius * radius")


class Rectangle:
    def area(self):
        print("Area of rectangle = length * breadth")


shape1 = Circle()
shape2 = Rectangle()

print("\n6. Polymorphism example")
shape1.area()
shape2.area()


# Quick revision:
# instance variable = separate value for each object
# class variable    = shared value for all objects
# encapsulation     = keeping data and methods together
# inheritance       = child class uses parent class features
# overriding        = child class changes parent class method
# polymorphism      = same method name, different behavior
