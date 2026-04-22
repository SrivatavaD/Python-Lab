# This program prints the multiplication table of a number N
# using a while loop.

# Ask the user to enter a number.
n = int(input("Enter a number: "))

# Start the counter from 1.
i = 1

# Run the loop until 10.
while i <= 10:
    print(n, "x", i, "=", n * i)

    # Increase the counter by 1 each time.
    i += 1

print("Numbers from 1 to 100:")

# This program prints numbers from 1 to 100 using a while loop.

# Start counting from 1.
number = 1

# Keep running the loop until the number becomes greater than 100.
while number <= 100:
    print(number)

    # Increase the number by 1 each time.
    number += 1

print("Search for a number in a tuple:")

# This tuple contains square numbers.
numbers_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# Ask the user which number they want to search.
x = int(input("Enter the number to search: "))

# Start checking from the first position.
index = 0
found = False

# Use a while loop to search for the number.
while index < len(numbers_tuple):
    if numbers_tuple[index] == x:
        print("Number found at index:", index)
        found = True
        break

    index += 1

# If the number was not found, show a message.
if not found:
    print("Number not found in the tuple.")
