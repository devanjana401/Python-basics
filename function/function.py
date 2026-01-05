# basic syntax-->
# def greet():
#     print("Hello, welcome to python!")
# greet()


# function with parameter
# def greet(name):
#     print(f"Hello,{name}")
# greet("Anjana")
# greet("Anju")


# using more arguments
# adding two number
# def add(num1,num2):
#     print(num1+num2)
# add(2,5)
# add(40,10)
# x=10
# y=20
# add(x,y)
# print(add(x,y))
# output-->
    # 7
    # 50
    # 30
    # 30
    # None


# return a value
# def add(num1,num2):
#     return num1+num2
# res=add(5,6)
# print(res)


# function to print numbers  to n
# def print_num(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# total=print_num(5)
# print(f"total: {total}")


# factorial of a number
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# num = int(input("Enter a number: "))
# print("Factorial =", factorial(num))


# fibonacci series
# def febi(n):
#     a,b =0,1          #0,1,1,2,3,5...
#     i=0
#     while i<n:
#         print(a,end=" ")
#         a,b = b,a+b 
#         i+=1
# num = int(input("Enter n: "))
# febi(num)


# using a default value
# example 1
# def add(a,b=1):       #b=1 is default parameter
#     print(a+b)
# add(3)

# example2
# def greet(name="Guest"):
#     print("Hello",name)
# greet()
# greet("Anju")


# keyword argument -- passing arguments as keyword
# def student(name,age,is_student=True):
#     print("Name:",name,"Age:",age,"is_student",is_student)
# student(is_student=False,age=20,name="Anu")  #for getting the order by using keyword
# student("Anju",23)  #by using this,we want to give dats as per keys order given on function


# variable number of arguments
# example 1
# def total(*numbers):           # * used for variable arguments
#     sum=0
#     for n in numbers:
#         sum+=n
#     return sum
# print(total(1,2,3,4))

# example 2
# def show_students(*students):
#     for i,student in enumerate(students,start=1):
#         print(f"\nStudent {i}:")
#         for key,value in student.items():
#             print(key,":",value)
# show_students(
#     {"name":"Anu","age":20,"grade":"A"},
#     {"name":"Anju","age":21,"grade":"B"},
#     {"name":"Anjana","age":22,"grade":"C"},
# )


# using **kwargs
# def info(**details):
#     for k,v in details.items():
#         print(f"{k}:{v}")
# info(name="Anu",age=20,city="kozhikode")
# info(name="Anu",age=20,city="kozhikode",email="anu@gmail.com")


# *args & **kwargs
# def student_details(*args, **kwargs):
#     print("Extra info:", args)     #tuple values
#     print("Student Details:")
#     for key, value in kwargs.items():
#         print(key, ":", value)
# student_details(                   #call with both
#     "Batch B1","Python Fullstack",name="Anju",age=22,grade="A",city="Delhi"
# )


def generate_bill(**items):
    print("Customer Bill")
    print("------------")
    total = 0
    for item, price in items.items():
        print(f"{item}: Rs.{price}")
        total += price
    print("-----------------------")
    print(f"Total Amount = Rs.{total}")

generate_bill(apple=50, orange=40, milk=30)
generate_bill(apple=50, orange=40, milk=30, bread=20)

