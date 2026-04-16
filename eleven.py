# A set in Python is a collection of unique values.
# Sets are written using curly brackets {}.

print("Set Example in Python")

# Creating sets
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "mango"}

print("Numbers set:", numbers)
print("Fruits set:", fruits)

# Sets do not allow duplicate values.
values = {1, 2, 2, 3, 4, 4}
print("Set without duplicates:", values)

# Sets are mutable, which means we can change them.
fruits.add("orange")
print("After add():", fruits)

fruits.remove("banana")
print("After remove():", fruits)

# Union combines all unique values from both sets.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)

# Intersection gives common values from both sets.
print("Intersection:", set_a & set_b)

# Important point:
# A set is mutable, but the items inside the set must be immutable.
# For example, numbers, strings, and tuples can be stored in a set.
valid_set = {1, "hello", (2, 3)}
print("Valid set:", valid_set)

print("Sets are mutable, but set elements must be immutable.")

# discard() removes an item if it exists.
# It does not give an error if the item is missing.
fruits.discard("apple")
print("After discard():", fruits)

# pop() removes and returns a random item from the set.
removed_item = fruits.pop()
print("Removed item using pop():", removed_item)
print("After pop():", fruits)

# copy() creates a new set with the same values.
fruits_copy = fruits.copy()
print("Copy of fruits set:", fruits_copy)

# clear() removes all items from the set.
fruits_copy.clear()
print("After clear() on copied set:", fruits_copy)
