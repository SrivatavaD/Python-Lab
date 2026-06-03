def sum(a,b):
    # and b are local variables
    c = a + b
    z = 1 # it creates a local variable z which is destroyed after this function returns.
    return c

def greet():
    z = 32 #local variable 
    print("Hello")
z = 9 # z is a global variable
print(sum(4,6))
print(z)