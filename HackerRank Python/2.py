# The provided code stub reads an integer,n, from STDIN. For all non-negative integers ,i<n  print i^2 .
# Example
# The list of non-negative integers that are less than   n = 3 is [0,1,2] . Print the square of each number on a separate line.

# n = int(input("Enter the number: "))
# for i in range(n):
#     print(i**2)

    # Without using any string methods, try to print the following:
    #  123...n

n = int(input())
for n in range(1,n+1): print(n,end="")

