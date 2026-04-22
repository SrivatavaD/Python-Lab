# Loops in Python are used to repeat a block of code.
# They help us avoid writing the same code again and again.

print("Loops in Python")

# 1. For loop
# A for loop is used when we want to repeat something a fixed number of times.
print("For loop example:")

# range(1, 6) gives numbers from 1 to 5.
for i in range(1, 6):
    print(i)

# A for loop can also be used with a list.
print("For loop with list:")
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# 2. While loop
# A while loop runs as long as the condition is True.
print("While loop example:")
count = 1

while count <= 5:
    print(count)
    
    # Increase the value by 1 each time.
    # Without this, the loop would run forever.
    count += 1

# 3. Nested loop
# A nested loop means a loop inside another loop.
print("Nested loop example:")

# The outer loop runs 3 times.
for i in range(1, 4):
    print("Outer loop:", i)

    # The inner loop runs 2 times for each outer loop.
    for j in range(1, 3):
        print(" Inner loop:", j)

# 4. Nested loop with multiplication table
# Here, the outer loop chooses the table number
# and the inner loop multiplies it with numbers from 1 to 3.
print("Nested loop with multiplication table:")

for i in range(1, 4):
    print("Table of", i)
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)

# 5. Nested loop for pattern printing
# The outer loop controls the rows.
# The inner loop prints stars in each row.
print("Pattern using nested loop:")

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

# 6. While loop example with repeated message
# This shows that a while loop can repeat text too.
print("While loop with message:")
message_count = 1

while message_count <= 3:
    print("Python is easy to learn")
    message_count += 1
