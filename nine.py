# Lists and tuples are both used to store multiple values in Python.
# But they have some important differences.

print("Difference Between List and Tuple")

# 1. Syntax difference
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)

print("List example:", list_example)
print("Tuple example:", tuple_example)

# 2. Mutability difference
# Lists can be changed after they are created.
list_example[0] = 100
print("Changed list:", list_example)

# Tuples cannot be changed after they are created.
# For example, tuple_example[0] = 100 would give an error.
print("Tuple remains unchanged:", tuple_example)

# 3. Methods difference
# Lists have many methods like append(), remove(), pop(), and sort().
fruits_list = ["apple", "banana"]
fruits_list.append("mango")
print("List after append():", fruits_list)

# Tuples have fewer methods like count() and index().
fruits_tuple = ("apple", "banana", "mango", "banana")
print("Count of banana in tuple:", fruits_tuple.count("banana"))
print("Index of mango in tuple:", fruits_tuple.index("mango"))

# 4. Use case difference
# Use a list when values may change.
shopping_list = ["milk", "bread", "eggs"]
shopping_list.append("butter")
print("Shopping list:", shopping_list)

# Use a tuple when values should stay fixed.
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Days of week tuple:", days_of_week)

# 5. In simple words
print("List = changeable collection")
print("Tuple = unchangeable collection")
