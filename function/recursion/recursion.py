# Recursion - function calling itself

# example 1
def countdown(n):
    if n==0:           #base case for break the function or it loops infinitely
        print("Lift Off")
    else:
        print(n)
        countdown(n-1)
countdown(5)

# example 2
# factorial
# factorial(0) = 1
# factorial(n) = n * factorial(n-1)
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# example 3
# sum of natural numbers
def sum_natural(n):
    if n==0:
        return 1
    else:
        return n + sum_natural(n-1)
print(sum_natural(5))

# example 4
# fibonacci 
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1)+fib(n-2)
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(6):
    print(fibonacci(i),end=" ")

# example 5
# reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))