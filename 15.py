# `break` and `continue` are used to control loops in Python.

print("Break and Continue in Python")

# 1. break example with for loop
# `break` stops the loop completely when the condition becomes true.
print("Break example with for loop:")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Explanation:
# The loop prints 1, 2, and 3.
# When i becomes 4, break stops the loop.

# 2. continue example with for loop
# `continue` skips the current iteration and moves to the next one.
print("Continue example with for loop:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Explanation:
# The loop skips 3 and prints 1, 2, 4, and 5.

# 3. break example with while loop
print("Break example with while loop:")
count = 1

while count <= 5:
    if count == 4:
        break
    print(count)
    count += 1

# Explanation:
# The loop stops as soon as count becomes 4.

# 4. continue example with while loop
print("Continue example with while loop:")
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)

# Explanation:
# When count becomes 3, that turn is skipped.
# So the loop prints 1, 2, 4, and 5.

# In simple words:
print("break = stops the loop completely")
print("continue = skips one turn and moves to the next")
