# example 1 - object in python
# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def start(self):
#         print(f"{self.color} {self.model} car is starting...")

# # creating objects
# car1 = Car("Red", "Toyota")
# car2 = Car("black", "Maruthi")

# car1.start()
# print(car1.color,car1.model)
# car2.start()
# print(car2.color,car2.model)
# print(id(car1))
# print(id(car2))


# example 2 - 
class Product:
    # constructor (used to initialize object values)
    def __init__(self, name, price, quantity):           # when a object created,__init__method automatically invoke(it doesn't call anywhere)
        self.name = name          # instance variable    
        self.price = price        # instance variable  
        self.quantity = quantity  # instance variable
        print(f"{self.name} object created..")

    # member function (method)
    def display_product(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def total_value(self):

        return self.price * self.quantity

# creating objects
product1 = Product("Pen", 10, 5)         # when object created there is memory reference that is self(eg:-product1,...)
product2 = Product("Notebook", 50, 3)
product3 = Product("pencil", 5, 13)

product1.display_product()
product2.display_product()
print(product1.name)

print("Total value of product1:", product1.total_value())
