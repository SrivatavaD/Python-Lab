# Abstraction in Python
# ---------------------
# Abstraction means hiding unnecessary internal details
# and showing only the important features to the user.
#
# In simple words:
# Abstraction = show what an object does, hide how it does it
#
# Example:
# When we use a TV remote, we press the power button.
# We do not need to know how the circuit works inside the remote.


from abc import ABC, abstractmethod


print("Abstraction in Python")
print("---------------------")


# 1. Basic abstraction example
# ABC means Abstract Base Class.
# @abstractmethod is used to create an abstract method.
#
# An abstract class cannot be used directly to create an object
# if it has an abstract method.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick.")


car1 = Car()
bike1 = Bike()

print("\n1. Basic abstraction example")
car1.start()
bike1.start()


# This would give an error because Vehicle is an abstract class:
# vehicle1 = Vehicle()


# 2. Shape area example
# Every shape has an area, but every shape calculates area differently.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of rectangle:", self.length * self.breadth)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle:", 3.14 * self.radius * self.radius)


rectangle1 = Rectangle(10, 5)
circle1 = Circle(7)

print("\n2. Shape area example")
rectangle1.area()
circle1.area()


# 3. Child class must define abstract method
# If a child class does not define the abstract method,
# Python will not allow us to create its object.
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


dog1 = Dog()

print("\n3. Child class defines abstract method")
dog1.sound()


# This would give an error because Cat does not define sound():
# class Cat(Animal):
#     pass
#
# cat1 = Cat()


# 4. Abstract class with normal method
# An abstract class can have normal methods and abstract methods.
class Payment(ABC):
    def payment_info(self):
        print("Payment process started.")

    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI.")


class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using card.")


upi_payment = UpiPayment()
card_payment = CardPayment()

print("\n4. Abstract class with normal method")
upi_payment.payment_info()
upi_payment.pay(500)

card_payment.payment_info()
card_payment.pay(1000)


# 5. Employee salary example
# Every employee gets salary, but salary calculation can be different.
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(self.name, "salary:", self.monthly_salary)


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate_per_hour):
        super().__init__(name)
        self.hours = hours
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        print(self.name, "salary:", self.hours * self.rate_per_hour)


full_time_employee = FullTimeEmployee("Aman", 40000)
part_time_employee = PartTimeEmployee("Riya", 80, 300)

print("\n5. Employee salary abstraction example")
full_time_employee.calculate_salary()
part_time_employee.calculate_salary()


# 6. Notification example
# Every notification sends a message, but the sending process is different.
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email sent:", message)


class SmsNotification(Notification):
    def send(self, message):
        print("SMS sent:", message)


email_notification = EmailNotification()
sms_notification = SmsNotification()

print("\n6. Notification abstraction example")
email_notification.send("Your order is confirmed.")
sms_notification.send("Your OTP is 1234.")


# 7. File operation example
# Every file operation performs an action, but each action works differently.
class FileOperation(ABC):
    @abstractmethod
    def execute(self):
        pass


class OpenFile(FileOperation):
    def execute(self):
        print("File opened successfully.")


class SaveFile(FileOperation):
    def execute(self):
        print("File saved successfully.")


class CloseFile(FileOperation):
    def execute(self):
        print("File closed successfully.")


open_file = OpenFile()
save_file = SaveFile()
close_file = CloseFile()

print("\n7. File operation abstraction example")
open_file.execute()
save_file.execute()
close_file.execute()


# Quick revision:
# abstraction      = hide unnecessary details and show important features
# abstract class   = class used as a base class
# abstract method  = method that child classes must define
# ABC              = Abstract Base Class
# @abstractmethod  = decorator used to create an abstract method
