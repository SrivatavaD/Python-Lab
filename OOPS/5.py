# Polymorphism in Python
# ----------------------
# Polymorphism means same name, different behavior.
#
# In simple words:
# Polymorphism = one method name, many forms
#
# Example:
# Car starts with a key.
# Bike starts with a kick.
# Laptop starts with a power button.
#
# The method name can be same: start()
# But the behavior can be different for each class.


print("Polymorphism in Python")
print("----------------------")


# 1. Basic polymorphism example
# Both classes have the same method name: sound()
# But both give different output.
class Dog:
    def sound(self):
        print("Dog barks.")


class Cat:
    def sound(self):
        print("Cat meows.")


dog1 = Dog()
cat1 = Cat()

print("\n1. Basic polymorphism example")
dog1.sound()
cat1.sound()


# 2. Polymorphism with loop
# Python calls the correct start() method
# depending on the object.
class Car:
    def start(self):
        print("Car starts with a key.")


class Bike:
    def start(self):
        print("Bike starts with a kick.")


class Laptop:
    def start(self):
        print("Laptop starts with a power button.")


items = [Car(), Bike(), Laptop()]

print("\n2. Polymorphism with loop")
for item in items:
    item.start()


# 3. Polymorphism with function
# The same function show_area() works for different objects.
class Circle:
    def area(self):
        print("Area of circle = pi * r * r")


class Rectangle:
    def area(self):
        print("Area of rectangle = length * breadth")


def show_area(shape):
    shape.area()


circle1 = Circle()
rectangle1 = Rectangle()

print("\n3. Polymorphism with function")
show_area(circle1)
show_area(rectangle1)


# 4. Polymorphism with inheritance
# Child classes can override the parent class method.
class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Cow(Animal):
    def sound(self):
        print("Cow says moo.")


class Lion(Animal):
    def sound(self):
        print("Lion roars.")


animals = [Cow(), Lion()]

print("\n4. Polymorphism with inheritance")
for animal in animals:
    animal.sound()


# 5. Method overriding and polymorphism
# Method overriding means child class changes the parent class method.
class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a button.")


vehicle1 = Vehicle()
bus1 = Bus()

print("\n5. Method overriding and polymorphism")
vehicle1.start()
bus1.start()


# 6. Polymorphism with built-in function
# Python's len() function works differently for different objects.
print("\n6. Polymorphism with built-in len() function")
print("Length of string:", len("Python"))
print("Length of list:", len([10, 20, 30]))
print("Length of dictionary:", len({"name": "Aman", "age": 21}))


# 7. Polymorphism with operators
# The + operator works differently with numbers and strings.
print("\n7. Polymorphism with + operator")
print("Number addition:", 10 + 20)
print("String joining:", "Hello " + "Python")


# 8. Employee work example
# Same method name work(), but different employees work differently.
class Developer:
    def work(self):
        print("Developer writes code.")


class Designer:
    def work(self):
        print("Designer creates UI designs.")


class Tester:
    def work(self):
        print("Tester checks the software.")


employees = [Developer(), Designer(), Tester()]

print("\n8. Employee work polymorphism example")
for employee in employees:
    employee.work()


# 9. Payment processing example
# Same method name pay(), but payment method is different.
class CashPayment:
    def pay(self, amount):
        print("Paid", amount, "using cash.")


class OnlinePayment:
    def pay(self, amount):
        print("Paid", amount, "using online payment.")


class CreditCardPayment:
    def pay(self, amount):
        print("Paid", amount, "using credit card.")


payments = [CashPayment(), OnlinePayment(), CreditCardPayment()]

print("\n9. Payment polymorphism example")
for payment in payments:
    payment.pay(500)


# 10. Same function for different objects
# The function print_details() can work with any object
# that has a details() method.
class Student:
    def details(self):
        print("Student name: Aman")


class Teacher:
    def details(self):
        print("Teacher name: Sharma Sir")


def print_details(person):
    person.details()


student1 = Student()
teacher1 = Teacher()

print("\n10. Same function for different objects")
print_details(student1)
print_details(teacher1)


# Quick revision:
# polymorphism      = same name, different behavior
# method overriding = child class changes parent class method
# same method name  = can work differently for different classes
