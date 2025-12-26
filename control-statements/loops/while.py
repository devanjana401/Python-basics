# # print numbers 1 to 5
# i = 1
# while(i<=5):
#     print(i)
#     i+=1
# print("done")

# # print numbers 5 to 1
# i = 5
# while(i>=1):
#     print(i)
#     i-=1
# print("done")

# # print even numbers b/w 1 to 10
# i = 1
# while(i<=10):
#     if (i%2==0):
#         print(i)
#     i+=1

# # factorial of number
# n=int(input("Enter a number :"))
# i=1
# fact = 1
# while(i<=n):
#     fact*=i
#     i+=1
# print(f"factorial of a number",fact)

# guess the number game
# secret=7
# guess=0
# while True:
#     guess = int(input("Enter your guess:"))
#     if(guess==secret):
#         print("Congrats....")
#         break
#     else:
#         print("Wrong...please try again")

# loop through array
arr = [10,33,44,66,77]
i = 0
while(i<len(arr)):
    print(arr[i])
    i+=1
