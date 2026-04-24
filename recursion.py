# Recursion in Python
# -------------------
# Recursion means a function calls itself.
#
# We use recursion when a problem can be broken into smaller versions
# of the same problem.
#
# Every recursive function should have:
# 1. Base case: the stopping condition
# 2. Recursive case: the function calls itself with a smaller value


print("Recursion in Python")


# Example 1: Countdown
# This function prints numbers from n down to 1.
def count_down(n):
    # Base case:
    # If n becomes 0, stop the recursion.
    if n == 0:
        print("Done")
        return

    # Recursive case:
    # Print the current number, then call the same function with n - 1.
    print(n)
    count_down(n - 1)


print("Countdown example:")
count_down(5)


# Example 2: Factorial using recursion
# Factorial means multiplying a number by all positive numbers below it.
# Example:
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    # Base case:
    # Factorial of 0 and 1 is 1.
    if n == 0 or n == 1:
        return 1

    # Recursive case:
    # n! = n * (n - 1)!
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


# How factorial(5) works:
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120


# Example 3: Sum of numbers using recursion
# This function returns the sum from 1 to n.
# Example:
# sum_numbers(5) = 5 + 4 + 3 + 2 + 1 = 15
def sum_numbers(n):
    # Base case:
    # If n is 0, there is nothing left to add.
    if n == 0:
        return 0

    # Recursive case:
    # Add n to the sum of all numbers below n.
    return n + sum_numbers(n - 1)


print("Sum from 1 to 5:", sum_numbers(5))


# Example 4: A simple power function
# This function calculates base raised to exponent.
# Example:
# power(2, 3) = 2 * 2 * 2 = 8
def power(base, exponent):
    # Base case:
    # Any number raised to power 0 is 1.
    if exponent == 0:
        return 1

    # Recursive case:
    # base^exponent = base * base^(exponent - 1)
    return base * power(base, exponent - 1)


print("2 raised to power 3:", power(2, 3))


# Important note:
# Without a base case, recursion will continue forever.
# Python stops it with a RecursionError.
#
# Example of wrong recursion:
#
# def wrong_function():
#     wrong_function()
#
# Do not call this function because it has no stopping condition.
