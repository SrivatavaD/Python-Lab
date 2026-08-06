def calculator(operator,a,b):
    # Write your code here
    if operator == '+':
        print(a + b)

    if operator == '-':
        print(a - b)

    if operator == '*':
        print(a * b)

    if operator == '/':
        print(a // b)

x = int(input())
y = int(input())

x = x - 1
y = y + 1

print("Value of X decremented by 1:", x)
print("Value of Y incremented by 1:", y)


# Write your code here
a = int(input())
b = int(input())
c = int(input())
d = int(input())

percentage = (a + b + c + d) / 4

print(round(percentage))