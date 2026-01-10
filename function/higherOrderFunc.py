# higher order function - a function takes another function as arguments

# example 1
def greet(name):
    return f"Hello, {name}!"
def morning(name):
    return f"Good morning,{name}"
def welcome_message(func,user_name):
    # func is another function passed as argument
    message = func(user_name)
    print(message)
# passing 'greet' function to 'welcome_message'
welcome_message(greet,"Anjana")
welcome_message(morning,"Anjana")

# example 2
def chef(recipe):
    print("Cooking is processing...")
    dish=recipe()
    print("Dish is ready...")
    return dish
def make_pasta():
    return "Pasta"
def make_pizza():
    return "Pizza"
print(chef(make_pasta))
print(chef(make_pizza))


# a function return another function

# example 1
def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
test = make_multiplier(4)
print(test(5))

# example 2
def create_discount(percent):
    def discount(price):
        return price - (price*percent/100)
    return discount
student_discount=create_discount(15)
normal_discount=create_discount(5)
employee_discount=create_discount(20)

print("student1 discount : ",student_discount(500))
print("student2 discount : ",student_discount(800))
print("normal discount : ",normal_discount(500))
print("employee discount : ",employee_discount(400))


# builtin higher order function - map,filter,reduce,sorted

# 1 - map
def square(x):
    return x*x
def double(x):
    return x*2
numbers = [1,2,3,4]
result1 = list(map(square,numbers))
result2 = list(map(double,numbers))
# using lambda
result3 = list(map(lambda n:n*n,numbers))
result4 = list(map(lambda n:n*2,numbers))
print(list(result1))
print(list(result2))
print(list(result3))
print(list(result4))

# 2 - filter
def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2!=0
def gt_5(n):
    return n>5
numbers=[1,2,3,4,5,6,7,8]
result_even = list(filter(is_even,numbers))
result_odd = list(filter(is_odd,numbers))
result_gt = list(filter(gt_5,numbers))
# using lambda
result_even1 = list(filter(lambda n:n%2==0,numbers))
result_odd1 = list(filter(lambda n:n%2!=0,numbers))
result_gt1 = list(filter(lambda n:n>5,numbers))
print(result_even)
print(result_odd)
print(result_gt)
print(result_even1)
print(result_odd1)
print(result_gt1)

# 3 - reduce
# add up all numbers in a list
from functools import reduce
def add(a,b):
    return a+b
numbers=[1,2,3,4,5,6,7,8]
result_reduce = reduce(add,numbers)
# using lambda
result_reduce1 = reduce(lambda a,b:a+b,numbers)
result_reduce_Mul = reduce(lambda a,b:a*b,numbers)
print(result_reduce)
print(result_reduce1)
print(result_reduce_Mul)

# 4 - sorted with key
students = [("Anu",22),("Anju",24),("Anjana",20)]
# sort by age
sorted_students = sorted(students,key=lambda x:x[1])
print(sorted_students)