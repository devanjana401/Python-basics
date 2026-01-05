# 1. print numbers from 1 to 10
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()


# 2. print even numbers between 1 and 20
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2
print()


# 3. sum of first 10 natural numbers
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum:", total)


# 4. factorial of a number
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)


# 5. reverse a number
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed Number:", rev)


# 6. count digits in a number
num = 56789
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digit Count:", count)


# 7. fibonacci series up to n terms
n = 10
a, b = 0, 1
i = 1
while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
print()


# 8. check palindrome number
num = 121
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if num == rev else "Not Palindrome")


# 9. multiplication table
n = 5
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


# 10. guess the number game
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess the number: "))
print("Correct!")


# 11. multiples of 3 between 1 and 50
i = 1
while i <= 50:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
print()


# 12. sum of even numbers between 1 and 100
i = 2
total = 0
while i <= 100:
    total += i
    i += 2
print("Even Sum:", total)


# 13. print numbers from 50 down to 1
i = 50
while i >= 1:
    print(i, end=" ")
    i -= 1
print()


# 14. largest digit in a number
num = 92841
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10
print("Largest Digit:", largest)


# 15. count digit occurrences
num = 122333
find = 3
count = 0
while num > 0:
    if num % 10 == find:
        count += 1
    num //= 10
print("Count:", count)


# 16. print digits in reverse order
num = 456
while num > 0:
    print(num % 10, end=" ")
    num //= 10
print()


# 17. ask user until positive number entered
num = -1
while num <= 0:
    num = int(input("Enter a positive number: "))
print("Accepted:", num)


# 18. sum of digits of a number
num = 345
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of Digits:", total)


# 19. number triangle
i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1


# 20. fibonacci series until last number < 1000
a, b = 0, 1
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
