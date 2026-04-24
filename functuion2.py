# More Details About Functions in Python
# --------------------------------------
# This file continues from the basic function examples in function.py.
# Here we learn some deeper function concepts.


print("More function concepts in Python")


# 1. Local variables
# A variable created inside a function is called a local variable.
# It can be used only inside that function.
def show_local_variable():
    message = "I am inside the function"
    print(message)


show_local_variable()

# If you try to print message outside the function, Python will give an error:
# print(message)


# 2. Global variables
# A variable created outside all functions is called a global variable.
# It can be read inside a function.
school_name = "Green Valley School"


def show_school_name():
    print("School:", school_name)


show_school_name()


# 3. Returning multiple values
# A function can return more than one value.
# Python returns them together as a tuple.
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication


add_result, sub_result, mul_result = calculate(10, 5)
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)


# 4. Function with type hints
# Type hints show what type of values a function expects.
# They do not force the type, but they make the code easier to understand.
def get_full_name(first_name: str, last_name: str) -> str:
    return first_name + " " + last_name


name = get_full_name("Aman", "Sharma")
print("Full name:", name)


# 5. Function with a docstring
# A docstring explains what a function does.
# It is written inside triple quotes just below the function line.
def find_area_of_rectangle(length, width):
    """Return the area of a rectangle."""
    return length * width


area = find_area_of_rectangle(8, 4)
print("Area of rectangle:", area)


# 6. *args
# *args lets a function accept any number of positional arguments.
# Python collects those values into a tuple.
def add_many_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


print("Total of many numbers:", add_many_numbers(2, 4, 6, 8, 10))


# 7. **kwargs
# **kwargs lets a function accept any number of keyword arguments.
# Python collects those values into a dictionary.
def show_student_details(**details):
    for key, value in details.items():
        print(key, ":", value)


print("Student details:")
show_student_details(name="Riya", age=19, course="Python", city="Delhi")


# 8. Nested function
# A nested function is a function written inside another function.
# It is useful when a small helper function is needed only in one place.
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()


outer_function()


# 9. Passing a function as an argument
# In Python, functions can be passed to other functions like normal values.
def double(number):
    return number * 2


def apply_function(function_name, value):
    return function_name(value)


print("Applying double function:", apply_function(double, 6))


# 10. Lambda function
# A lambda is a short one-line function.
# It is useful for simple tasks.
cube = lambda number: number * number * number

print("Cube of 3:", cube(3))


# 11. Function using a list
# A function can receive a list and work with all its items.
def find_highest_score(scores):
    highest = scores[0]

    for score in scores:
        if score > highest:
            highest = score

    return highest


marks = [72, 88, 91, 67, 95, 80]
print("Highest score:", find_highest_score(marks))


# 12. Practice task
# Try writing your own function below.
# Task: Create a function named find_lowest_score.
# It should take a list of scores and return the lowest score.


def find_lowest_score(scores):
    lowest = scores[0]

    for score in scores:
        if score < lowest:
            lowest = score

    return lowest


print("Lowest score:", find_lowest_score(marks))


# 13. Function to find the factorial of a number
# Factorial means multiplying a number by all positive numbers below it.
# Example: 5 factorial means 5 * 4 * 3 * 2 * 1 = 120
# It is written as 5!
def factorial(n):
    result = 1

    for number in range(1, n + 1):
        result = result * number

    return result


print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))
