# method 1 -- import

# import calculator
# print(calculator.add(2,4))
# print(calculator.subtract(4,2))
# print(calculator.multiply(1,4))
# print(calculator.divide(10,5))


# method 2 -- import specific functions

# from calculator import add,subtract
# print(add(4,6))
# print(subtract(6,4))


# method 3 -- import module as another simple name

# import calculator as calc
# print(calc.add(2,4))
# print(calc.subtract(8,6))


# method 4 -- import all functions(not recommended - it makes conflicts)

from calculator import *
print(add(2,2))