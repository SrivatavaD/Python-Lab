# A dictionary in Python is used to store data in key-value pairs.
# It is written using curly brackets {}.

print("Dictionary Example in Python")

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print("Student dictionary:", student)

# Accessing values using keys
print("Student name:", student["name"])
print("Student age:", student["age"])

# Changing an existing value
student["age"] = 22
print("After changing age:", student)

# Adding a new key-value pair
student["city"] = "Delhi"
print("After adding city:", student)

# Another example of a dictionary
car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2024
}

print("Car dictionary:", car)

# keys() returns all the keys in the dictionary.
print("Student keys:", student.keys())

# values() returns all the values in the dictionary.
print("Student values:", student.values())

# items() returns all key-value pairs.
print("Student items:", student.items())

# get() is used to safely get the value of a key.
print("Student course using get():", student.get("course"))

# update() is used to add or change multiple values at once.
student.update({"age": 23, "grade": "A"})
print("After update():", student)
