# 1. Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than , print Not Weird

# import math
# import os
# import random
# import re
# import sys
# n = int(input("Enter the number: "))

# if(n % 2 != 0):
#     print("Weird")
# elif(n % 2 == 0 and n >= 2 and n <= 5):
#     print("Not Weird")
# elif(n % 2 == 0 and n >= 6 and n <= 20):
#     print("Weird")
# else:
#     print("Not Weird")


# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# a = int(input())
# b = int(input())
# print(a+b);
# print(a-b);
# print(a*b);


# Task
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)
