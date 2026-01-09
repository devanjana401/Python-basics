# shorter syntax,and also used creating new list from existing list
# it includes-->
# expression
# item
# iterable
# condition

# example 1
nums=[]
for i in range(1,6):
    nums.append(i)
print(nums)

# using list comprehension
numbers = [x for x in range(1,6)]
print(numbers)

# example 2
squares = [x**2 for x in range(1,6)]
print(squares)

# example 3
evensquare = [x**2 for x in range(1,6) if x%2==0]
print(evensquare)

# example 4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#  Example 5: Convert Strings to Uppercase
fruits = ["apple", "banana" , "orange"]
u_friuts = [fruit.upper() for fruit in fruits ] 
print(u_friuts)


#Create pairs (x, y) where x is from [1, 2] and y is from [3, 4].
# normal
ss=[]
for x  in [1,2]:
    for  y in  [3,4]:
        ss.append((x,y))
print(ss)
# Example 6: Nested Loops in List Comprehension
#[1, 2]    [3, 4]   out: [(1, 3), (1, 4), (2, 3), (2, 4)]
pairs=[(x,y) for x in [1,2] for y in [3,4]]
print(pairs)

# Example 7: Filtering with Condition
names=["Anu", "Riya", "Krishna","Amith", "Akshay"]
long_nmaes=[name for name in names if len(name)>4]
print(long_nmaes)

#Example 8: Flatten a Nested List
matrix=[[1,2,3],[4,5,6],[7,8,9]]
# normal 
f=[]
for row in matrix:
    for num in row:
        f.append(num)
print(f)
flattened = [num for row in matrix for num in row ]
print(flattened)

# Example 9: Using a Function Inside
def square(n):
    return n**2
result = [square(x) for x in range(1,6)]
result2 = [(lambda x:x**2) (x) for x in range(1,6)]
print(result)
print(result2)

#Example 10: Replace Normal Characters
text = "I Love Python"
m_text= [ch if ch!=" " else "-" for ch in text]
print(m_text)
print("".join(m_text))

#Example 11: Dictionary & Set Comprehension
squares = {x:x**2 for x in range(5)}
print(squares)

unique = {x for x in [1,2,2,3,3,4,5]}
print(unique)

# %%writefile mymodule.py
def greet(name):
    return f"Hello, {name}! Welcome to Python Modules."
pi = 3.14159

