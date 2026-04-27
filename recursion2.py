# More Recursion Examples in Python
# ---------------------------------
# This file gives more practice with recursion.
#
# Remember:
# A recursive function must have:
# 1. A base case, where the function stops
# 2. A recursive case, where the function calls itself


print("More recursion examples in Python")


# Example 1: Print numbers from 1 to n
# This is the opposite of countdown.
def print_numbers(n):
    # Base case:
    # If n becomes 0, stop the function.
    if n == 0:
        return

    # First call the function for smaller numbers.
    print_numbers(n - 1)

    # Then print the current number.
    # This prints numbers in increasing order.
    print(n)


print("Numbers from 1 to 5:")
print_numbers(5)


# Example 2: Reverse a string using recursion
# We take the last character and then reverse the remaining string.
def reverse_string(text):
    # Base case:
    # If the string is empty or has only one character, it is already reversed.
    if len(text) <= 1:
        return text

    # Recursive case:
    # Last character + reverse of everything before the last character.
    return text[-1] + reverse_string(text[:-1])


print("Reverse of Python:", reverse_string("Python"))


# Example 3: Fibonacci number using recursion
# Fibonacci series:
# 0, 1, 1, 2, 3, 5, 8, 13 ...
#
# Each number is the sum of the two previous numbers.
def fibonacci(n):
    # Base cases:
    # fibonacci(0) is 0
    # fibonacci(1) is 1
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case:
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci number at position 6:", fibonacci(6))


# Example 4: Sum of digits using recursion
# Example:
# 1234 = 1 + 2 + 3 + 4 = 10
def sum_of_digits(number):
    # Base case:
    # If number is a single digit, return it.
    if number < 10:
        return number

    # number % 10 gives the last digit.
    # number // 10 removes the last digit.
    return number % 10 + sum_of_digits(number // 10)


print("Sum of digits of 1234:", sum_of_digits(1234))


# Example 5: Count digits using recursion
# Example:
# 98765 has 5 digits.
def count_digits(number):
    # Base case:
    # Any number from 0 to 9 has one digit.
    if number < 10:
        return 1

    # Remove the last digit and count again.
    return 1 + count_digits(number // 10)


print("Number of digits in 98765:", count_digits(98765))


# Example 6: Find the greatest common divisor using recursion
# GCD means the greatest number that divides both numbers exactly.
# Example:
# GCD of 20 and 12 is 4.
def gcd(a, b):
    # Base case:
    # If b becomes 0, a is the answer.
    if b == 0:
        return a

    # Recursive case:
    # Keep replacing a with b and b with the remainder.
    return gcd(b, a % b)


print("GCD of 20 and 12:", gcd(20, 12))


# Example 7: Check if a word is a palindrome using recursion
# A palindrome reads the same forward and backward.
# Examples: madam, level, noon
def is_palindrome(word):
    # Base case:
    # Empty string or one letter is always a palindrome.
    if len(word) <= 1:
        return True

    # If first and last letters are different, it is not a palindrome.
    if word[0] != word[-1]:
        return False

    # Check the middle part of the word.
    return is_palindrome(word[1:-1])


print("Is madam a palindrome?", is_palindrome("madam"))
print("Is python a palindrome?", is_palindrome("python"))


# Example 8: Find the sum of a list using recursion
# Example:
# [10, 20, 30] = 10 + 20 + 30 = 60
def sum_list(numbers):
    # Base case:
    # If the list is empty, the sum is 0.
    if len(numbers) == 0:
        return 0

    # First item + sum of the remaining list.
    return numbers[0] + sum_list(numbers[1:])


marks = [10, 20, 30, 40]
print("Sum of list:", sum_list(marks))


# Example 9: Find the largest number in a list using recursion
def find_largest(numbers):
    # Base case:
    # If there is only one number, it is the largest.
    if len(numbers) == 1:
        return numbers[0]

    # Find the largest number in the remaining list.
    largest_in_rest = find_largest(numbers[1:])

    # Compare the first number with the largest number from the rest.
    if numbers[0] > largest_in_rest:
        return numbers[0]
    return largest_in_rest


scores = [45, 89, 72, 96, 55]
print("Largest score:", find_largest(scores))


# Example 10: Binary search using recursion
# Binary search works only on a sorted list.
# It repeatedly checks the middle element.
def binary_search(numbers, target, start, end):
    # Base case:
    # If start becomes greater than end, the target is not present.
    if start > end:
        return -1

    middle = (start + end) // 2

    # If the middle value is the target, return its index.
    if numbers[middle] == target:
        return middle

    # If target is smaller, search in the left half.
    if target < numbers[middle]:
        return binary_search(numbers, target, start, middle - 1)

    # If target is bigger, search in the right half.
    return binary_search(numbers, target, middle + 1, end)


sorted_numbers = [3, 8, 12, 19, 25, 31, 42]
target_number = 25
position = binary_search(sorted_numbers, target_number, 0, len(sorted_numbers) - 1)
print("Position of 25:", position)
