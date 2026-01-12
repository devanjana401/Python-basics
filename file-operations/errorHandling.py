# handling runtime errors
# try:
#     with open("nofile.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File was not found")


# basic structure
# try:
#     # code that might cause an error
# except:
#     # what to do if an error happen

# example 1
# try:
#     num = int(input("Enter a number:"))
#     print(10/num)
# except:
#     print("Ooops!Spmething went wrong")

# example 2
# try:
#     num = int(input("Enter a number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Please enter a valid number")

# example 3 -- we can also additionally use 'else' and 'finally'
try:
    num = int(input("Enter a number:"))
    result = 10/num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number")
else:
    print("Success! Result is:",result)
finally:
    print("Program finished")