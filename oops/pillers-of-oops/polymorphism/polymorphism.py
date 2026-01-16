# method overriding(polymorphism using inheritance)
# Method overriding happens when a child class has a method with the same name as a method in the parent class but a different implementation. 
class Animal: 
    def sound(self): 
        print("Animal makes a sound") 
class Dog(Animal): 
    def sound(self): 
        print("Dog barks") 
class Cat(Animal): 
    def sound(self): 
        print("Cat meows") 
def make_sound(animal): 
    animal.sound() 
make_sound(Dog()) 
make_sound(Cat())


# duck typing(polymorphism without inheritance)
class Duck: 
    def quack(self): 
        print("Duck: Quack")  
class Person: 
    def quack(self): 
        print("Person: I can also imitate quack") 
def make_it_quack(obj): 
    obj.quack() 
make_it_quack(Duck()) 
make_it_quack(Person())


# operator overloading
# Operator overloading means using the same operator for different types of objects. 
# For example: 
# ● 10 + 20 → adds numbers 
# ● "A" + "B" → joins strings 
# ● 2*3=6 
# ● “A”*3 =AAA