# Strings are used to store text in Python.
# A string can be written inside single quotes or double quotes.

print("String Examples in Python")

# Creating strings
name = "Alice"
city = 'Delhi'
message = "Hello World"

print("Name:", name)
print("City:", city)
print("Message:", message)

# 1. Concatenation
# This joins two or more strings together.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Concatenation:", full_name)

# 2. Repetition
# This repeats a string multiple times.
word = "Hi "
print("Repetition:", word * 3)

# 3. Indexing
# This accesses one character from the string.
text = "Python"
print("First character:", text[0])
print("Second character:", text[1])

# 4. Slicing
# This takes a part of the string.
print("Slicing 0 to 3:", text[0:3])
print("Slicing 2 to 6:", text[2:6])

# 5. Length
# `len()` tells us how many characters are in the string.
print("Length of text:", len(text))

# 6. Uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 7. Replace
# This replaces one part of the string with another.
greeting = "Hello"
print("Replace example:", greeting.replace("H", "J"))

# 8. Find
# This gives the position of a character in the string.
print("Position of 't' in Python:", text.find("t"))

# 9. Checking content
# `isalpha()` checks if all characters are letters.
# `isdigit()` checks if all characters are numbers.
check_text = "python"
print("Is alphabet only?", check_text.isalpha())
print("Is digit only?", check_text.isdigit())

# 10. Membership
# This checks whether a character or word is present in the string.
print("Is 'H' in Hello?", "H" in greeting)
print("Is 'z' in Hello?", "z" in greeting)


# Some useful string functions

# 11. endswith()
# This checks if the string ends with a given word or character.
sentence = "I am learning Python"
print("Does the sentence end with 'Python'?", sentence.endswith("Python"))

# 12. capitalize()
# This makes the first letter capital and the rest small.
small_text = "python programming"
print("Capitalize example:", small_text.capitalize())

# 13. replace()
# This replaces one word or character with another.
fruit_text = "I like mango"
print("Replace function:", fruit_text.replace("mango", "apple"))

# 14. find()
# This finds the position of a word or character in the string.
language_text = "Python is easy"
print("Find function:", language_text.find("is"))

# 15. count()
# This counts how many times a word or character appears.
repeat_text = "apple apple banana apple"
print("Count function:", repeat_text.count("apple"))
