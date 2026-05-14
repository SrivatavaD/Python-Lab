#Function is a block of code that performs a specific tasks when it is called.

# def calculateGmean(a,b):
#     Gmean = (a*b)/(a+b)
#     print(Gmean)

# def isgreater(a,b):
#     if(a>b):
#         print("The first number is greater than the second number.")
#     else:
#         print("the second number is greater than the first number.")    

# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: ")) 

# isgreater(a,b)
# calculateGmean(a,b)  

# def average(a,b):
#     print("the average is: " , (a+b)/2)
# average(4,10)   
# 
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
        # print("the average is: ", sum/len(numbers))
        return sum/len(numbers)
c = average(4,15)  
print(c)       

