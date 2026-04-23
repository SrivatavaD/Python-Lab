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
