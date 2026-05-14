# str = "hello"
# print(str.upper())
# print(str.isupper())

# a = int(input("enter the number: "))
# print (a)

# applePrice = 10
# budget = 100
# if(budget - applePrice > 50):
#     print("You can buy the apple")
# else:
#     print("you cannot buy the apple")

# num = int(input("Enter the number: "))
# if(num < 0):
#     print("Negative number")
# elif(num > 0):
#     if(num <=10):
#         print("number is between 1 and 10")
#     elif(num>10 and num<=20):
#         print("number is between 11 and 20")
#     else:
#         print("number is greater than 20")
# else:
#     print("Number is zero")           
       
# use of time module in python
# import time
# timestamp = time.strftime('%H:%M:%S')
# print("Current time is:", timestamp)
# if timestamp >= "05:00:00" and timestamp < "11:00:00":
#     print("Good Morinng")
# else:
#     print("Sleep weell")

#use of break statement is not cumplusory in python
# for loops in python

# for k in range(5):
#     print(k+1)

# for k in range(1,20):
#     print(k)    
    
# for k in range(1,10,2):
#     print(k)

# i = int(input("Enter the number: "))
# while(i<=38):
#     i = int(input("Enter the number: "))
#     print(i)
# print("Done with the loop")    

# count = 50 
# while(count >0):
#     print(count)
#     count = count - 1
# else:
#     print("Done with the loop") 
# 

for i in range(12):
    if(i==10):
        break
    print("5 X", i+1, "=", 5*(i+1))

print("Done with the loop")

