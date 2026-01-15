# basic syntax

class Parent: 
    # parent class 
    def parent_method(self): 
        print("This is the parent method.") 
class Child(Parent): 
    # child class 
    def child_method(self): 
        print("This is the child method.") 
# Create object of Child 
obj = Child() 
obj.parent_method()  # inherited from Parent 
obj.child_method()   
# defined in Child 


# example 1
class Vehicle: 
    def __init__(self, brand): 
        self.brand = brand 
     
    def start_engine(self): 
        print(f"{self.brand} engine started.") 
 
# Child class inherits from Vehicle 
class Car(Vehicle): 
    def __init__(self, brand, model): 
        super().__init__(brand)  # Call parent constructor 
        self.model = model 
     
    def show_details(self): 
        print(f"Car: {self.brand} {self.model}") 
 
# Create an object of Car 
my_car = Car("Toyota", "Corolla") 
my_car.start_engine()   # Inherited from Vehicle 
my_car.show_details()   # Defined in Car 


# example 2 - method overriding
class Animal: 
    def make_sound(self): 
        print("Some generic sound") 
 
class Dog(Animal): 
    def make_sound(self): 
        print("Bark Bark!") 
 
dog = Dog() 
dog.make_sound() 


# example 3 - single inheritance
class Parent: 
    def greet(self): 
        print("Hello from Parent") 
 
class Child(Parent): 
    def play(self): 
        print("Child is playing")

    
# example 4 - multilevel inheritance
class Grandfather: 
    def house(self): 
        print("Owns a big house") 
 
class Father(Grandfather): 
    def car(self): 
        print("Owns a car") 
 
class Son(Father): 
    def bike(self): 
        print("Owns a bike") 
obj = Son()
obj.house()
obj.car()
obj.bike()


# example 5 - multiple inheritance
class Father: 
    def skills(self): 
        print("Skilled in driving") 
 
class Mother: 
    def skills(self): 
        print("Skilled in cooking") 
 
class Child(Father, Mother): 
    def show_skills(self): 
        super().skills()  # Calls Father's version (MRO - method resolution order) - first priority 
        print("Also skilled in painting") 
 
obj = Child() 
obj.show_skills()


# example 6 - using upper() keyword
class Employee: 
    def __init__(self, name): 
        self.name = name 
 
    def show_info(self): 
        print(f"Employee Name: {self.name}") 
 
class Manager(Employee): 
    def __init__(self, name, department): 
        super().__init__(name)  # calling parent constructor 
        self.department = department 
 
    def show_info(self): 
        super().show_info()  # calling parent method 
        print(f"Department: {self.department}") 
 
mgr = Manager("Anupama", "IT") 
mgr.show_info() 


# example 7 - school system
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
 
    def display(self): 
        print(f"Name: {self.name}, Age: {self.age}") 
 
class Student(Person): 
    def __init__(self, name, age, grade): 
        super().__init__(name, age) 
        self.grade = grade 
 
    def display(self): 
        super().display() 
        print(f"Grade: {self.grade}") 
 
class Teacher(Person): 
    def __init__(self, name, age, subject): 
        super().__init__(name, age) 
        self.subject = subject 
 
    def display(self): 
        super().display() 
        print(f"Subject: {self.subject}") 
 
# Create objects 
student1 = Student("Vivaan", 10, "5th") 
teacher1 = Teacher("Anupama", 30, "Computer Science") 
 
student1.display() 
print("----") 
teacher1.display() 