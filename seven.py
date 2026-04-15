# A list in Python is used to store multiple values in one variable.
# Lists are written inside square brackets [].

print("List Example in Python")

# Creating lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed_data = ["Alice", 25, 5.6, True]

print("Fruits list:", fruits)
print("Numbers list:", numbers)
print("Mixed data list:", mixed_data)

# Lists are ordered, which means items stay in sequence.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Lists are mutable, which means we can change their values.
fruits[1] = "orange"
print("After changing banana to orange:", fruits)

# Adding a new item to the list using append()
fruits.append("grapes")
print("After adding grapes:", fruits)

# Removing an item from the list using remove()
fruits.remove("apple")
print("After removing apple:", fruits)

# Length of the list using len()
print("Length of numbers list:", len(numbers))

# Lists can also contain duplicate values.
colors = ["red", "blue", "red"]
print("List with duplicate values:", colors)
