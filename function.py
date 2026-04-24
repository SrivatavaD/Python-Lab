# Functions in Python are blocks of code that perform a specific task.
# They help us avoid repeating the same code again and again.

print("Functions in Python")

# 1. Simple function
# `def` is used to create a function.
def greet():
    print("Hello")

# Calling the function
greet()

# 2. Function with parameter
# A parameter is a value that we pass into a function.
def greet_name(name):
    print("Hello", name)

# Calling the function with an argument
greet_name("Aman")

# 3. Function with return value
# `return` sends the result back from the function.
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# 4. Function to find the average of three numbers
def find_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Calling the function
average = find_average(10, 20, 30)
print("Average:", average)

# 5. Function to subtract two numbers
def subtract(a, b):
    return a - b

print("Subtraction:", subtract(10, 4))

# 6. Function to find the square of a number
def square(number):
    return number * number

print("Square:", square(6))

# 7. Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("7 is", check_even_odd(7))
print("12 is", check_even_odd(12))

# 8. Function to print a message multiple times
def print_message(message, times):
    for i in range(times):
        print(message)

print("Message function example:")
print_message("Python is fun", 3)

# 9. Function with default argument
# A default argument gives a value automatically if no value is passed.
def welcome(name="Guest"):
    print("Welcome", name)

print("Default argument example:")
welcome()
welcome("Riya")

# 10. Function with keyword arguments
# Keyword arguments let us pass values using the parameter names.
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

print("Keyword argument example:")
student_info(course="Python", name="Aman", age=21)
