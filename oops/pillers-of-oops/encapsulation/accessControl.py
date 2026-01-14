# Python uses three types of access control: 
# 1. Public 
# 2. Protected 
# 3. Private 
# These control how data and methods can be accessed inside or outside a class.


# public members
class Student: 
    def __init__(self, name): 
        self.name = name   # public variable 

s = Student("Rahul") 
print(s.name) 


# protected members - can access to diferrent clasess
class Student: 
    def __init__(self, name, age): 
        self._age = age     # protected variable 
 
s = Student("Rahul", 20) 
print(s._age) 


# private members
class Student: 
    def __init__(self, name, marks): 
        self.__marks = marks   # private variable 
 
s = Student("Rahul", 85) 
# print(s.__marks)   # This will give an error
# Private variables protect sensitive data. 