# File I/O in Python
# ------------------
# File I/O means File Input and Output.
#
# Input  = reading data from a file
# Output = writing data to a file
#
# Python uses the open() function to work with files.
# The best practice is to use "with open(...)" because it closes the file
# automatically after the work is done.


print("File I/O examples in Python")


# 1. Writing to a file
# Mode "w" means write.
# If the file does not exist, Python creates it.
# If the file already exists, Python overwrites its old content.
with open("notes.txt", "w") as file:
    file.write("Hello, this is my first file.\n")
    file.write("I am learning File I/O in Python.\n")

print("notes.txt created and written successfully.")


# 2. Reading the whole file
# Mode "r" means read.
with open("notes.txt", "r") as file:
    content = file.read()

print("Content of notes.txt:")
print(content)


# 3. Appending to a file
# Mode "a" means append.
# Append adds new content at the end of the file.
with open("notes.txt", "a") as file:
    file.write("This line was added later using append mode.\n")

print("New line appended to notes.txt.")


# 4. Reading line by line
# This is useful when a file has many lines.
print("Reading notes.txt line by line:")

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. Writing student information to a file
# We can store useful information in files.
with open("student.txt", "w") as file:
    file.write("Name: Aman\n")
    file.write("Age: 21\n")
    file.write("Course: Python\n")

print("student.txt created successfully.")


# 6. Reading student information
with open("student.txt", "r") as file:
    student_data = file.read()

print("Student details:")
print(student_data)


# 7. Using writelines()
# writelines() writes multiple strings into a file.
# Important: It does not add new lines automatically, so we add "\n".
subjects = ["Math\n", "Science\n", "English\n", "Computer\n"]

with open("subjects.txt", "w") as file:
    file.writelines(subjects)

print("subjects.txt created using writelines().")


# 8. Using readlines()
# readlines() reads all lines and stores them in a list.
with open("subjects.txt", "r") as file:
    subject_list = file.readlines()

print("Subjects list:")
print(subject_list)


# 9. Checking if a file exists before reading
# If we try to read a file that does not exist, Python gives an error.
# The os.path.exists() function helps us check first.
import os

file_name = "notes.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        print("File exists. First line is:")
        print(file.readline().strip())
else:
    print("File does not exist.")


# Common file modes:
# "r" = read
# "w" = write
# "a" = append
# "x" = create a new file, gives an error if the file already exists
