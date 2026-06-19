def my_decorator(func):
    def wrapper():
        print("Before functions runs")
        func()
        print("After function runs")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()