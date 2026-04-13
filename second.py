# This line shows the title of the program.
print("Simple Calculator")

# This line tells the user which math operations are allowed.
print("Operations: +, -, *, /")

# Ask the user to type the first number.
# `input()` reads what the user types as text, and `float()` changes it into a number.
num1 = float(input("Enter first number: "))

# Ask the user which operation they want to perform.
# For example: + for addition or * for multiplication.
operator = input("Enter operator: ")

# Ask the user to type the second number.
num2 = float(input("Enter second number: "))

# Check which operator the user entered.
# If it is +, add the two numbers.
if operator == "+":
    print("Result:", num1 + num2)

# If it is -, subtract the second number from the first.
elif operator == "-":
    print("Result:", num1 - num2)

# If it is *, multiply the two numbers.
elif operator == "*":
    print("Result:", num1 * num2)

# If it is /, divide the first number by the second.
elif operator == "/":
    # Division by zero is not allowed, so we check before dividing.
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

# If the user typed something other than +, -, *, or /,
# show an error message.
else:
    print("Invalid operator.")



#WAP to find the area of a square whose side is given by.
print("Area of the Sqaure")
side = float(input("Enter the side of the sqaure:"))
area = side * side
print("Area of the sqaure is:", area , "cm^2")

#WAP to input 2 floating point numbers & print their average.
print("Average of the two numbers")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
average = (num1 + num2) /2
print("The average of the two numbers is:", average)

#WAP to input 2 int numbers, a and b.
#Print True if a is greater than or equal to b. If not print False.
print("Comparison of the two numbers")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
result = a >= b
print("Is a greater than or equal to b?", result)
