# Purchase Discount
amount = float(input("Enter purchase amount: "))
if amount > 1000:
    print("Discounted price:", amount * 0.9)
else:
    print("No discount. Pay:", amount)

# Age Category
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

# Password Check
password = input("Enter password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# Number Check
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
if num > 50:
    print("Greater than 50")

# Electricity Bill
units = int(input("Enter electricity units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*7
else:
    bill = 100*5 + 100*7 + (units-200)*10
print("Total Bill: ₹", bill)

# Shopkeeper Discount
purchase = float(input("Enter purchase amount: "))
if purchase > 5000:
    print("20% discount. Pay:", purchase*0.8)
elif purchase > 2000:
    print("10% discount. Pay:", purchase*0.9)
else:
    print("No discount. Pay:", purchase)

# Triangle Classifier
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")

# Character Check
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")

# ATM Simulation
pin = input("Enter PIN: ")
if pin == "1234":
    print("Transaction Allowed")
else:
    print("Invalid PIN")

# ATM Withdrawal Simulator
pin = input("Enter PIN: ")
balance = float(input("Enter balance: "))
withdraw = float(input("Enter withdraw amount: "))
if pin == "1234":
    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawn. Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid PIN")

# Student Result with Grace Marks
marks = [int(input(f"Subject {i+1}: ")) for i in range(5)]
avg = sum(marks)/5
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 50:
    grade = "C"
elif avg >= 35:
    grade = "Pass with Grace"
else:
    grade = "Fail"
print("Grade:", grade)

# Online Shopping Cart
amount = float(input("Enter total purchase amount: "))
if amount > 10000:
    final = amount*0.75
elif 5000 < amount <= 10000:
    final = amount*0.85
elif 2000 < amount <= 5000:
    final = amount*0.95
else:
    final = amount
print("Final payable amount:", final)

# Marks-Based Scholarship
marks = int(input("Enter marks: "))
if marks >= 95:
    print("Full Scholarship")
elif marks >= 85:
    print("Half Scholarship")
elif marks >= 70:
    print("Quarter Scholarship")
else:
    print("No Scholarship")

# Water Usage Billing
liters = int(input("Enter water usage in liters: "))
if liters <= 1000:
    bill = liters*2
elif liters <= 5000:
    bill = liters*3
elif liters <= 10000:
    bill = liters*5
else:
    bill = liters*10
print("Total bill: ₹", bill)

# Username and Password Validation
username = input("Username: ")
password = input("Password: ")
if username=="admin" and password=="1234":
    print("Login successful")
elif username=="admin":
    print("Incorrect password")
else:
    print("Invalid user")

# Train Ticket Fare System
cls = input("Class (Sleeper/AC/First): ")
age = int(input("Age: "))
fare = 1000
if age < 5:
    fare = 0
elif 5 <= age <= 12:
    fare /= 2
elif age > 60:
    fare *= 0.7
print(f"Ticket Fare for {cls}: ₹{fare}")

# Voting Eligibility
age = int(input("Enter age: "))
nationality = input("Nationality: ")
if age >= 18:
    if nationality.lower()=="indian":
        print("Eligible to vote")
    else:
        print("Foreign nationals can't vote")
else:
    print("Not eligible due to age")

# Quadratic Equation Roots Finder
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("Real & distinct roots:", r1, r2)
elif d == 0:
    r = -b/(2*a)
    print("Real & equal roots:", r)
else:
    print("Imaginary roots")

# Bank Loan Approval System
salary = float(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))
if salary>=50000 and credit_score>=700:
    print("Loan Approved")
elif salary>=30000 and credit_score>=600:
    print("Partially Approved")
else:
    print("Loan Rejected")
