# class employee:
#     def __init__(self,  name, id):
#         self.name = name
#         self.id = id
#     def showdetails(self):
#         print(f"the name of the employee: {self.id} is {self.name}")

# class programmer(employee):
#     def showlanguage(self):
#         print("the default language is python")

# e1 = employee("Devansh", 400)
# e1.showdetails()
# e2 = employee("Harry" , 4100)
# e2.showdetails()        
# 
# Access Modifiers in python
# 
class employee:
    def __init__(self):
        self.__name = "devansh"
        
a = employee()   #print(a.name) # canniot be accessed directly

print(a._employee__name) # can be accessed indirectly 

print(a.__dir__())
        