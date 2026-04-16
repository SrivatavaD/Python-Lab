# A tuple in Python is used to store multiple values in one variable.
# It is similar to a list, but a tuple cannot be changed after it is created.

print("Tuple Example in Python")

# Creating tuples
numbers = (10, 20, 30, 40)
fruits = ("apple", "banana", "mango")
mixed_data = ("Alice", 25, 5.6, True)

print("Numbers tuple:", numbers)
print("Fruits tuple:", fruits)
print("Mixed data tuple:", mixed_data)

# Tuples are ordered, so we can access items using index numbers.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Tuples allow duplicate values.
colors = ("red", "blue", "red")
print("Tuple with duplicate values:", colors)

# A tuple with one item must have a comma after the value.
single_item = (5,)
print("Single item tuple:", single_item)
print("Type of single_item:", type(single_item))

# Tuples are immutable.
# This means we cannot change values like we do in a list.
# For example, fruits[0] = "orange" would give an error.

print("Tuples are useful when values should not change.")
