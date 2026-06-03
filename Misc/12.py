# def sum(a,b):
#     # and b are local variables
#     c = a + b
#     z = 1 # it creates a local variable z which is destroyed after this function returns.
#     return c

# def greet():
#     z = 32 #local variable 
#     print("Hello")
# z = 9 # z is a global variable
# print(sum(4,6))
# print(z)

# def greet():
#     print("Hello")

# def square(x):
#     return x*x
# print(square(50))

# def print_full_name(first_name, last_name):
#     return f"{first_name} {last_name}"
# print(print_full_name("John", "Doe"))

# add = lambda a,b: a+b
# print(add(3,5))

# square = lambda x:x*x
# list1 = [1,2,3,4,5]

# print(map(square, list1))

#to print the factoial of a number
# def factorial(n):
#     if n == 0 or n == 1:  # base case
#         return 1
#     return factorial(n-1)*n
# print(factorial(6))

# def sum_of_digits(n):
#     if n == 0:
#         return 0
    
#     return n%10 + sum_of_digits(n//10)

#sum of digits of 7532 is same as:
#2 (last digit) + sum of digits of 753

# print(sum_of_digits(7532))

# print(type(sum_of_digits))

# def increment():
#     counter = 0
#     counter += 1
#     print(counter)

# increment()

#Write a recursive function fib(n) that prints the first n fibonacci numbers.

# This function returns the fibonacci number at a given position.
# def fibonacci(num):
#     # Base case: the 0th fibonacci number is 0 and the 1st is 1.
#     if num == 0 or num == 1:
#         return num
    
#     # Recursive case: each fibonacci number is the sum of the previous two.
#     return fibonacci(num - 1) + fibonacci(num - 2)

# # This function prints the first n fibonacci numbers.
# def fib(n, i = 0):
#     # Stop when we have printed n numbers.
#     if i == n:
#         print()
#         return
    
#     # Print the fibonacci number at position i.
#     print(fibonacci(i), end=" ")
    
#     # Move to the next position using recursion.
#     fib(n, i + 1)

# # Print the first 10 fibonacci numbers.
# fib(100)

# Write a function safe_divide(a,b) that returns the results of a/b , but returns "Cannot Divide by zero" if b is 0.

# This function safely divides a by b.
def safe_divide(a, b):
    # If b is 0, division is not possible.
    if b == 0:
        return "Cannot Divide by zero"
    
    # If b is not 0, return the result of a divided by b.
    return a / b

# Calling the function with a valid divisor.
print(safe_divide(10, 2))

# Calling the function with 0 as divisor.
print(safe_divide(10, 0))

