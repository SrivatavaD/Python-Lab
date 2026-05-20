from pathlib import Path

file_path = Path(__file__).parent / "myfile.txt"

with open(file_path, "r") as f:
     lines = f.readlines()

maths = lines[0].split()[-1]
science = lines[1].split()[-1]
english = lines[2].split()[-1]

print(f"marks of student 1 in maths is: {maths}")
print(f"marks of student 1 in science is: {science}")
print(f"marks of student 1 in english is: {english}")
