# Public, Protected, and Private Functions in Python
# -------------------------------------------------
# In Python OOP, functions inside a class are called methods.
#
# Python uses naming rules to show how a method should be used:
#
# public method       = method_name()
# protected method    = _method_name()
# private method      = __method_name()
#
# Python does not make methods fully private like some other languages.
# It mainly trusts the programmer to follow these naming rules.


print("Public, Protected, and Private Functions in Python")
print("--------------------------------------------------")


# 1. Public function
# A public function can be used anywhere.
class PublicExample:
    def show_message(self):
        print("This is a public function.")


public_object = PublicExample()

print("\n1. Public function")
public_object.show_message()


# 2. Protected function
# A protected function starts with one underscore.
# It means this function is mainly for use inside the class
# or inside child classes.
class Student:
    def __init__(self, name):
        self.name = name

    def _show_name(self):
        print("Student name is:", self.name)


student1 = Student("Aman")

print("\n2. Protected function")
student1._show_name()


# 3. Private function
# A private function starts with two underscores.
# It cannot be called directly from outside the class.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __show_balance(self):
        print("Balance is:", self.balance)

    def account_details(self):
        self.__show_balance()


account1 = BankAccount(5000)

print("\n3. Private function")
account1.account_details()


# This line would give an error because __show_balance is private:
# account1.__show_balance()


# 4. Protected function with inheritance
# A child class can use a protected function from the parent class.
class Animal:
    def _eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def show_activity(self):
        self._eat()
        print("Dog is barking.")


dog1 = Dog()

print("\n4. Protected function with inheritance")
dog1.show_activity()


# 5. Private function with inheritance
# Private functions are not directly available in child classes.
class Parent:
    def __secret(self):
        print("This is private.")

    def show_secret(self):
        self.__secret()


class Child(Parent):
    def show_parent_secret(self):
        self.show_secret()


child1 = Child()

print("\n5. Private function with inheritance")
child1.show_parent_secret()


# This would give an error because __secret is private:
# child1.__secret()


# 6. Public, protected, and private in one class
class Example:
    def public_method(self):
        print("This is public.")

    def _protected_method(self):
        print("This is protected.")

    def __private_method(self):
        print("This is private.")

    def access_private(self):
        self.__private_method()


example1 = Example()

print("\n6. Public, protected, and private together")
example1.public_method()
example1._protected_method()
example1.access_private()


# Quick revision:
# public method    = can be used anywhere
# protected method = starts with _ and should be used inside class or child class
# private method   = starts with __ and should be used inside the same class
