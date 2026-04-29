# More File I/O Examples in Python
# --------------------------------
# File I/O means reading data from files and writing data to files.
#
# This file gives more practice examples using text files.


print("More File I/O examples in Python")


# 1. Create a file and write a daily task list
# Mode "w" creates a new file or overwrites an existing file.
with open("tasks.txt", "w") as file:
    file.write("1. Learn Python functions\n")
    file.write("2. Practice recursion\n")
    file.write("3. Study File I/O\n")

print("tasks.txt created successfully.")


# 2. Read the full file content
# read() reads the whole file as one string.
with open("tasks.txt", "r") as file:
    tasks = file.read()

print("Tasks:")
print(tasks)


# 3. Count the number of lines in a file
# Each line in the file is counted one by one.
line_count = 0

with open("tasks.txt", "r") as file:
    for line in file:
        line_count = line_count + 1

print("Number of lines in tasks.txt:", line_count)


# 4. Count the number of words in a file
# split() breaks a line into words.
word_count = 0

with open("tasks.txt", "r") as file:
    for line in file:
        words = line.split()
        word_count = word_count + len(words)

print("Number of words in tasks.txt:", word_count)


# 5. Append new data to a file
# Mode "a" adds new content at the end without deleting old content.
with open("tasks.txt", "a") as file:
    file.write("4. Revise examples\n")

print("New task added to tasks.txt.")


# 6. Read a file as a list of lines
# readlines() returns all lines inside a list.
with open("tasks.txt", "r") as file:
    task_lines = file.readlines()

print("Tasks as a list:")
print(task_lines)


# 7. Write student marks in CSV style
# CSV means comma-separated values.
# Example: name,subject,marks
with open("marks.csv", "w") as file:
    file.write("name,subject,marks\n")
    file.write("Aman,Python,88\n")
    file.write("Riya,Python,92\n")
    file.write("Kabir,Python,79\n")

print("marks.csv created successfully.")


# 8. Read CSV-style data line by line
print("Student marks:")

with open("marks.csv", "r") as file:
    for line in file:
        clean_line = line.strip()
        values = clean_line.split(",")
        print(values)


# 9. Copy content from one file to another
# First we read from tasks.txt, then we write the same content to backup_tasks.txt.
with open("tasks.txt", "r") as original_file:
    original_content = original_file.read()

with open("backup_tasks.txt", "w") as backup_file:
    backup_file.write(original_content)

print("tasks.txt copied to backup_tasks.txt.")


# 10. Handle missing file errors
# try-except helps us handle errors without crashing the program.
try:
    with open("unknown_file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("unknown_file.txt was not found.")


# 11. Create a simple report file
# We can use file writing to generate a report.
student_name = "Aman"
python_marks = 88
recursion_marks = 84
file_io_marks = 91
average_marks = (python_marks + recursion_marks + file_io_marks) / 3

with open("report.txt", "w") as file:
    file.write("Student Report\n")
    file.write("--------------\n")
    file.write("Name: " + student_name + "\n")
    file.write("Python Marks: " + str(python_marks) + "\n")
    file.write("Recursion Marks: " + str(recursion_marks) + "\n")
    file.write("File I/O Marks: " + str(file_io_marks) + "\n")
    file.write("Average Marks: " + str(average_marks) + "\n")

print("report.txt created successfully.")


# Common file modes:
# "r" = read
# "w" = write
# "a" = append
# "x" = create a new file only if it does not already exist
