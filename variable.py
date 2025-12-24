# 1. Variables are created by assigning a value
# Syntax: variable_name = value

name = "Anupama"     # stores text → string (str)
age = 28             # stores whole number → integer (int)
height = 5.4         # stores decimal number → float
is_student = True    # stores True/False → boolean (bool)

# 2. Python automatically detects the data type

# 3. Print variable values
print(name)
print(age)
print(height)
print(is_student)

# 4. Print with text
print("Name:", name)
print("Age:", age)
print("Height:", height)

# 5. Variable naming rules
# - Must start with letter or _
# - Can use letters, numbers, _
# - No spaces or special characters
# - Case-sensitive

# Valid names
student1 = True
_age = 25

# Invalid (examples)
# 2age = 28      ❌
# my name = "A"  ❌

# 6. Variable values can be changed
age = 28
print(age)

age = 29
print(age)
