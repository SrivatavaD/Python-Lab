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
