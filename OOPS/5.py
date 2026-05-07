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


# Quick revision:
# polymorphism      = same name, different behavior
# method overriding = child class changes parent class method
# same method name  = can work differently for different classes
