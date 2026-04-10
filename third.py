# This program shows how loops work in Python.
# A loop is used when we want to repeat something multiple times.

print("Loop Example Program")

# This is a `for` loop.
# It repeats the code block for each number in the range.
# `range(1, 6)` means the numbers 1, 2, 3, 4, and 5.
for number in range(1, 6):
    print("Current number:", number)

print("For loop has finished.")

# This is a `while` loop.
# It keeps running as long as the condition is True.
count = 1

# The loop will continue until `count` becomes greater than 3.
while count <= 3:
    print("Count is:", count)

    # Increase the value of `count` by 1 each time.
    # This is important, otherwise the loop would run forever.
    count += 1

print("While loop has finished.")
