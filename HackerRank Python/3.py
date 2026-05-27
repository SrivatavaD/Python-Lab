
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
# def is_leap(year):
#     leap = False

#     if year % 4 == 0:
#         leap = True

#         if year % 100 == 0:
#             leap = False

#             if year % 400 == 0:
#                 leap = True

#     return leap


# year = int(input())
# print(is_leap(year))

# List comprehensions are a concise way to create lists. They consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the context of the for

x = int(input()) 
y = int(input()) 
z = int(input()) 
n = int(input())

result = []

for i in range(x + 1): 
    for j in range(y + 1): 
        for k in range(z + 1): 
            if i + j + k != n: 
                result.append([i, j, k])

print(result)