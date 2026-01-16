# Abstarction - Showing only the important details and hiding the unnecessary internal details. 
# Eg:- A car: 
    # You use the steering wheel, brake, and accelerator. 
    # You do not see how the engine works inside. 
    # The complex mechanism is hidden from the driver.
# Python provides abstraction mainly through: 
    # 1. Abstract classes 
    # 2. Abstract methods 
    # 3. The abc module (Abstract Base Class)

# example 1
from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod 
    def sound(self): 
        pass     
# No implementation 
class Dog(Animal): 
    def sound(self): 
        print("Dog barks") 
class Cat(Animal): 
    def sound(self): 
        print("Cat meows") 
# Using the classes 
dog = Dog() 
cat = Cat() 
dog.sound() 
cat.sound()

# example 2 - bank atm
from abc import ABC, abstractmethod 
class ATM(ABC): 
    @abstractmethod 
    def withdraw(self, amount): 
        pass 
class SBI(ATM): 
    def withdraw(self, amount): 
        print("SBI ATM: You withdrew", amount)  
class HDFC(ATM): 
    def withdraw(self, amount): 
        print("HDFC ATM: You withdrew", amount) 
atm = SBI() 
atm.withdraw(1000) 