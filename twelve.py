# Sets and dictionaries both use curly brackets {},
# but they are different in structure and purpose.

print("Difference Between Set and Dictionary")

# 1. Set stores only values.
my_set = {1, 2, 3}
print("Set example:", my_set)

# 2. Dictionary stores key-value pairs.
my_dict = {"name": "Rahul", "age": 21}
print("Dictionary example:", my_dict)

# 3. Duplicate handling
# A set does not allow duplicate values.
duplicate_set = {1, 2, 2, 3}
print("Set without duplicates:", duplicate_set)

# A dictionary does not allow duplicate keys.
# If the same key is written again, the last value is kept.
duplicate_dict = {"a": 10, "b": 10, "a": 20}
print("Dictionary with duplicate key:", duplicate_dict)

# 4. Accessing data
# In a dictionary, values are accessed using keys.
student = {"name": "Aman", "age": 20, "course": "Python"}
print("Student dictionary:", student)
print("Student name:", student["name"])

# In a set, items are not accessed using keys like a dictionary.
colors = {"red", "blue", "green", "red"}
print("Set of colors:", colors)

# 5. Simple use case explanation
print("Set = collection of unique values")
print("Dictionary = collection of key-value pairs")
