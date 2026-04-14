# Conditional statements help a program make decisions.
# Python uses `if`, `elif`, and `else` for this.

print("Conditional Statement Example")

# Store a number in the variable `marks`.
marks = 75

# Check the first condition.
# If marks are 90 or more, this block will run.
if marks >= 90:
    print("Grade A")

# `elif` means "else if".
# This block runs only if the first condition was false.
elif marks >= 75:
    print("Grade B")

# `else` runs when none of the above conditions are true.
else:
    print("Grade C")

# Another simple example using age.
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Traffic light example.
Light = input("Light color : ")

if Light == "red":
    print("Stop")
elif Light == "yellow":
    print("Get Ready")
elif Light == "green":
    print("Go")
else:
    print("Invalid color")

#Ternary operator is a one line if else statement.
age  = int(input("Enter your age: "))
result = "Adult" if age >=  18 else "Minor"  
print(result)    


# Type conversion means changing a value from one data type to another.
# This is useful when we want to use the data in a different way.

print("Type Conversion Example")

# Here, "25" is stored as text, so Python treats it as a string.
number_text = "25"
print("Original value:", number_text)
print("Original type:", type(number_text))

# Convert the string into an integer.
number_int = int(number_text)
print("After int() conversion:", number_int)
print("Type after conversion:", type(number_int))

# Convert the integer into a float.
number_float = float(number_int)
print("After float() conversion:", number_float)
print("Type after conversion:", type(number_float))

# Convert the integer back into a string.
number_string = str(number_int)
print("After str() conversion:", number_string)
print("Type after conversion:", type(number_string))
