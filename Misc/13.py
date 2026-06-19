# def my_decorator(func):
#     def wrapper():
#         print("Before functions runs")
#         func()
#         print("After function runs")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello!")
# say_hello()

# login check code
def login_required(func):
    def wrapper(user):
        if user == "admin":
            func(user)
        else:
            print("Access Denied.")
    return wrapper
@login_required
def dashboard(user):
    print(f"welcome to the dashboard, {user}")
dashboard("admin")
dashboard("guest")