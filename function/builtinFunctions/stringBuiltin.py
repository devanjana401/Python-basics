# len

# Create a string variable and store some text in it
s = "Python String and variable"
# Converts all letters in the string to lowercase
print("Lowercase:", s.lower())       
# Converts all letters in the string to uppercase
print("Uppercase:", s.upper())        
# Converts the first letter of each word to uppercase
print("Title Case:", s.title())      
# Converts only the first letter of the string to uppercase, rest to lowercase
print("Capitalize:", s.capitalize()) 
# Swaps the case of each letter (uppercase becomes lowercase and vice versa)
print("Swapcase:", s.swapcase())     
# Similar to lower(), but more powerful for case-insensitive comparisons (used for languages with special characters)
print("Casefold:", s.casefold())

# Create a string with extra spaces at the beginning and end
s = "   Hello Python   "
# Print the original string using repr() to clearly show spaces
print("Original:", repr(s))          
# Removes spaces from both the beginning and the end of the string
print("strip():", repr(s.strip()))   
# Removes spaces only from the left side (beginning) of the string
print("lstrip():", repr(s.lstrip()))  
# Removes spaces only from the right side (end) of the string
print("rstrip():", repr(s.rstrip()))

# create a string variable with some text
s = "Hello world,Hello world"
# print the original string
print("Original:",s)
# Replace the word 'world with 'python using replace() method
print("Replace 'world' with 'python':",s.replace("world","Python"))
print(s)

# create a string with words separated by commas
s =  "apple,banana,cherry"
# print original string
print("original:",s)
# split the string into a list using comma (',') as the separate
print("split by comma:",s.split(","))
# create a list of words
words = ["Python","is","fun"]
# join list elements into a single string separated by a space
print("join with space:"," ".join(words))

# find the path from right
path = "/home/user/documents/file.txt"
lslash = path.rfind("/")
filename = path[lslash+1:]
print(filename)

# find
s = "Hello world"
# finds the first position(index) of 'o' from the left  side of string
print("Find 'o':",s.find("o"))        #output:4
# finds the last position(index) of 'o' from the right  side of string
print("Find 'o'from right:",s.rfind("o"))       #output:7
# finds the position (index) of 'w' in the string
print("Index 'w'",s.index("w"))       #output:6

# count
s ="banana"
# count how many times the letter 'a' apperas in the string
print("Count 'a':",s.count("a"))     #output:3

# start or end 
s = "python"
# check if the string starts with 'py'
print("Starts with 'py':",s.startswith("py"))
# check if the string ends with 'on'
print("Ends with 'on':",s.endswith("on"))

# checking characters
s1 = "Hello"
s2 = "123"
s3 = "Hello123"
s4 = "   "  # String containing only spaces
# Check if all characters in s1 are alphabet letters
print("s1.isalpha():", s1.isalpha())   
# Check if all characters in s2 are digits
print("s2.isdigit():", s2.isdigit())   
# Check if all characters in s3 are alphanumeric (letters or numbers)
print("s3.isalnum():", s3.isalnum())  
# Check if s4 contains only whitespace
print("s4.isspace():", s4.isspace())   
# Check if s1 follows title case (first letter uppercase, rest lowercase)
print("s1.istitle():", s1.istitle())   
# Check if all letters in s1 are uppercase
print("s1.isupper():", s1.isupper())  
# Check if all letters in s1 are lowercase
print("s1.islower():", s1.islower())

# padding
s1 = "42"
s2 = "567"
# zFill(width) -> pads the string with zeros on left to reach total width
print("zFill(5):",s1.zfill(5))       #output:'00042'
print("zFill(5):",s2.zfill(5))       #output:'00567'
# center(width,fillchar) -> centers the string in a field of given width,opationally filling with a character
# here we use space ' ' as a fill character
print("center(6,''):",s1.center(20, '-'))
# ljust -> left-justifies the string and fills right with specified character
print("ljust(6, ' '):",s1.ljust(20, '-'))
# rjust -> right-justifies the string and fills left with specified character
print("ljust(6, ' '):",s1.rjust(20, '-'))


# Sample data: student ID, name, and marks
students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 23, "name": "Bob", "marks": 92},
    {"id": 7, "name": "Charlie", "marks": 78},
    {"id": 15, "name": "Diana", "marks": 100}
]
def get_marks(student):
    return student['marks']
# Sort students by marks (descending)   
students_sorted=sorted(students,reverse=True,key=get_marks)
title="Student Report Card"
print("\n"+ title.center(40,"="))
print("ID".center(6),"Name".ljust(15),"Marks".rjust(5))
print("-"*40)
for student in students_sorted:
    student_id = str(student['id']).zfill(3)
    name=student['name'].ljust(15)
    marks=str(student['marks']).rjust(5)
    print(student_id.center(6),name,marks)
print("="*40)

# partition
s = "Hello-World-python"
print("Partition:",s.partition("-"))         # output:('Hello', '-', 'World-python')
print("RPartition:",s.rpartition("-"))       # output:('Hello-World', '-', 'python')

# encoding
s = "Hello"
encodeed = s.encode()
print("Encoded:",encodeed)       
# output:b'Hello'

# removePrefix,removeSuffix