# def average(a,b,c):
#     d = (a + b + c) / 3
#     # print(d)
#     return d
# o1 = average(1,2,3)    
# o2 = average(4,5,6)
# print(o1)
# print(o2)

# def add(a,b):
#     x =  a+b
#     return x
# c = add(1,2)
# print(c)

# Lambda Functions in Python
# square = lambda x: x * x

# """as good as writing 
# def sum(x,y):
#     return x+y """
# sum = lambda x,y:x+y
# print(square(5))
# print(sum(3,6))

# recursion functions:

# to print the fibonacci series
def fib(n):
    # base case of recursion
    if(n == 0 or n ==1):
        return n
    return fib(n-2) + fib(n-1)

print(fib(5))
