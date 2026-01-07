# decorators used to add extra features in function

# example 1
def greet_decorator(func):
    def wrapper():
        print("Hello,this is before the function")
        func()
        print("Hello,this is after the function")
    return wrapper
@greet_decorator
def say_hello():
    print("Hello,this is the original function")
say_hello()