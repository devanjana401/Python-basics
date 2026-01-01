# for i in range(6):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)


# -----sum of 1 to n numbers-----
# n = int(input("Enter the number:"))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# ------for list-----
# list1 = [10,20,30,40]
# # print(list1[0])
# # print(list1[1])
# # print(list1[2])
# # print(list1[3])
# for i in list1:
#     print(i)


# ------for string-----
# str1 = "Hello"
# for char in str1:
#     print(char)

# -----for getting index and value-----
# for index,value in enumerate(list1):
#     print(index,value)

# -----we can add starting index value in enumerate-----
# fruits = ["Apple","Banana","Orange"]
# for index,fruit in enumerate(fruits,start=1):
#     print(index,fruit)

# -----sum of list-----
# marks = [30,50,28,40]
# total_mark = 0
# for mark in marks:
#     total_mark+=mark
# print(f"Totatl mark = {total_mark}")

# -----largest number-----
# marks = [30,50,28,40]
# largest = marks[0]
# for mark in marks:
#     if(mark>largest):
#         largest = mark
# print(f"Largest mark = {largest}")

# -----smallest number-----
# marks = [30,50,28,40]
# smallest = marks[0]
# for mark in marks:
#     if(mark<smallest):
#         smallest = mark
# print(f"Smallest mark = {smallest}")

# -----second largest number-----
# marks = [30, 50, 28, 40]
# largest = marks[0]
# second_largest = marks[0]
# for mark in marks:
#     if mark > largest:
#         second_largest = largest
#         largest = mark
#     elif mark > second_largest and mark != largest:
#         second_largest = mark
# print(f"Second Largest mark = {second_largest}")


# -----for loop in dictionary-----

# -----getting key and value from a dictionary-----
# student = {"name":"Anjana","age":23,"grade":"A"}
# for i in student:
#     print(i,student[i])

# for getting values only
# student = {"name":"Anjana","age":23,"grade":"A"}
# for i in student.values():
#     print(i)

# for getting both key and value
# student = {"name":"Anjana","age":23,"grade":"A"}
# for key,value in student.items():
#     print(key,value)


# -----reverse a string-----
# 1-using[::-1]
# 2-
# word = "Anjana"
# reverse = ''
# for char in word:
#     reverse = char+reverse
# print(f"Reverse:{reverse}")

# checking given string is palindrome
# word = input("Enter the word:")
# reverse = ''
# for char in word:
#     reverse=char+reverse
# print(f"Reverse: {reverse}")
# if word==reverse:      # word[::-1]:
#     print(f"{word} is palindrome")
# else:
#     print(f"{word} is not a palindrome")


# -----nested for loops-----

# for i in range(4):
#     for j in range(4):
#         print("* ",end="")
#     print()
# output-->
    # * * * * 
    # * * * * 
    # * * * *
    # * * * *


# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,"",end="")
#     print()
# output-->
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5