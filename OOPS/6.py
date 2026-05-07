# Inheritance in Python
# ---------------------
# Inheritance means one class can use the properties
# and methods of another class.
#
# In simple words:
# Inheritance = child class gets features from parent class
#
# Parent class = base class
# Child class  = derived class


print("Inheritance in Python")
print("---------------------")


# 1. Basic inheritance example
# Child class can use methods of Parent class.
class Parent:
    def show_parent(self):
        print("This is parent class.")


class Child(Parent):
    def show_child(self):
        print("This is child class.")


child1 = Child()

print("\n1. Basic inheritance example")
child1.show_parent()
child1.show_child()


# 2. Animal example
# Dog gets eat() method from Animal class.
class Animal:
    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


dog1 = Dog()

print("\n2. Animal inheritance example")
dog1.eat()
dog1.bark()


# 3. Constructor in inheritance
# A child class can call the parent class constructor using super().
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


student1 = Student("Aman", "Python")

print("\n3. Constructor in inheritance")
student1.show_name()
student1.show_course()


# 4. Method overriding
# If child class writes a method with the same name as parent class method,
# it is called method overriding.
class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")


car1 = Car()

print("\n4. Method overriding")
car1.start()


# 5. Single inheritance
# One child class inherits from one parent class.
class SingleParent:
    def show_single_parent(self):
        print("Single parent class.")


class SingleChild(SingleParent):
    def show_single_child(self):
        print("Single child class.")


single_child = SingleChild()

print("\n5. Single inheritance")
single_child.show_single_parent()
single_child.show_single_child()


# 6. Multiple inheritance
# One child class inherits from more than one parent class.
class Father:
    def father_property(self):
        print("Father property.")


class Mother:
    def mother_property(self):
        print("Mother property.")


class FamilyChild(Father, Mother):
    def child_property(self):
        print("Child property.")


family_child = FamilyChild()

print("\n6. Multiple inheritance")
family_child.father_property()
family_child.mother_property()
family_child.child_property()


# 7. Multilevel inheritance
# Inheritance happens in a chain.
class Grandfather:
    def grandfather_property(self):
        print("Grandfather property.")


class FatherInChain(Grandfather):
    def father_property(self):
        print("Father property.")


class ChildInChain(FatherInChain):
    def child_property(self):
        print("Child property.")


chain_child = ChildInChain()

print("\n7. Multilevel inheritance")
chain_child.grandfather_property()
chain_child.father_property()
chain_child.child_property()


# 8. Hierarchical inheritance
# Multiple child classes inherit from one parent class.
class CommonAnimal:
    def eat(self):
        print("Animal is eating.")


class PetDog(CommonAnimal):
    def bark(self):
        print("Dog is barking.")


class Cat(CommonAnimal):
    def meow(self):
        print("Cat is meowing.")


pet_dog = PetDog()
cat1 = Cat()

print("\n8. Hierarchical inheritance")
pet_dog.eat()
pet_dog.bark()

cat1.eat()
cat1.meow()


# 9. Hybrid inheritance
# Hybrid inheritance is a combination of two or more inheritance types.
class BasePerson:
    def show_person(self):
        print("Person details.")


class SchoolStudent(BasePerson):
    def show_student(self):
        print("Student details.")


class Sports:
    def show_sports(self):
        print("Sports details.")


class SportsStudent(SchoolStudent, Sports):
    def show_all(self):
        print("Sports student details.")


sports_student = SportsStudent()

print("\n9. Hybrid inheritance")
sports_student.show_person()
sports_student.show_student()
sports_student.show_sports()
sports_student.show_all()


# Quick revision:
# inheritance        = child class gets features from parent class
# parent class       = class that gives features
# child class        = class that receives features
# super()            = used to call parent class constructor or method
# method overriding  = child class changes parent class method
# single inheritance = one parent and one child
# multiple inheritance = more than one parent
# multilevel inheritance = inheritance in a chain
# hierarchical inheritance = one parent and many children
# hybrid inheritance = combination of inheritance types
