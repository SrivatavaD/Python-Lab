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
