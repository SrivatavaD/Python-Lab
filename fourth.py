# Type casting means changing one data type into another.
# This is useful when we want to use data in a different way.

print("Type Casting Example in Python")

# Here, "10" is stored as text, so its type is string.
x = "10"
print("Value of x:", x)
print("Type of x:", type(x))

# Convert the string into an integer using int().
y = int(x)
print("Value of y after int(x):", y)
print("Type of y:", type(y))

# Convert the integer into a decimal number using float().
z = float(y)
print("Value of z after float(y):", z)
print("Type of z:", type(z))

# Convert the integer into a string using str().
a = str(y)
print("Value of a after str(y):", a)
print("Type of a:", type(a))

# Convert a number into boolean using bool().
# Any non-zero number becomes True.
b = bool(y)
print("Value of b after bool(y):", b)
print("Type of b:", type(b))
