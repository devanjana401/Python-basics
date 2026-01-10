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

# example 2 - decorator with arguments
def my_decorator(func): 
    def wrapper(*args, **kwargs): 
        print("Before function") 
        result = func(*args, **kwargs) 
        print("After function") 
        return result 
    return wrapper 
@my_decorator 
def add(a, b): 
    return a + b 
print(add(10, 20)) 

# example 3 - logging
def log(func): 
    def wrapper(*args, **kwargs): 
        print("Function name:", func.__name__) 
        return func(*args, **kwargs) 
    return wrapper 
@log 
def multiply(a, b): 
    return a * b 
print(multiply(4, 5)) 

# example 4 - checking login before access
def require_login(func): 
    def wrapper(user): 
        if user == "admin": 
            return func(user) 
        else: 
            print("Access denied") 
            return wrapper 
@require_login 
def dashboard(user): 
    print("Welcome to dashboard,", user) 
dashboard("admin") 
dashboard("guest") 

# example 5 - decorator with return values
def uppercase(func): 
    def wrapper(): 
        result = func() 
        return result.upper() 
    return wrapper 
@uppercase 
def message(): 
    return "hello students" 
print(message()) 

# example 6 - multiple decorators
def star(func): 
    def wrapper(): 
        print("*****") 
        func() 
        print("*****") 
        return wrapper 
def hash(func): 
    def wrapper(): 
        print("#####") 
        func() 
        print("#####") 
    return wrapper 
@star 
@hash 
def show(): 
    print("Content") 
show()