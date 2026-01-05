# 1. shopping cart total
prices = [120, 250, 75, 300, 150]
total = 0
for p in prices:
    total += p
print("Total Bill:", total)


# 2. counting fruits
fruits = ["apple", "banana", "apple", "mango", "apple", "orange"]
count = 0
for f in fruits:
    if f == "apple":
        count += 1
print("Apple Count:", count)


# 3. average marks
marks = [78, 85, 69, 90, 88]
total = 0
for m in marks:
    total += m
avg = total / len(marks)
print("Average Marks:", round(avg, 2))


# 4. fuel efficiency
mileage = [15, 16, 14, 17, 15, 16]
total = 0
for m in mileage:
    total += m
avg = total / len(mileage)
print("Average Mileage:", avg)
print("Status:", "Good" if avg > 15 else "Needs check")


# 5. discounted prices (10%)
prices = [200, 450, 300, 150, 600]
discounted = []
for p in prices:
    discounted.append(p - (p * 0.10))
print("Discounted Prices:", discounted)


# 6. count adults
ages = [12, 18, 20, 14, 25, 30]
adults = 0
for age in ages:
    if age >= 18:
        adults += 1
print("Adults Count:", adults)


# 7. electric bill
units = [100, 250, 400, 150]
for u in units:
    rate = 5 if u <= 200 else 7
    print(f"Units: {u}, Bill: {u * rate}")


# 8. longest word
words = ["python", "data", "development", "AI"]
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print("Longest Word:", longest)


# 9. vowel count (user input)
sentence = input("Enter a sentence: ").lower()
vowels = 0
for ch in sentence:
    if ch in "aeiou":
        vowels += 1
print("Vowel Count:", vowels)


# 10. attendance
attendance = ["Present", "Absent", "Present", "Present", "Absent"]
present = absent = 0
for a in attendance:
    if a == "Present":
        present += 1
    else:
        absent += 1
print("Present:", present, "Absent:", absent)

# 11. print 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()


# 12. odd numbers 1–20
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")
print()


# 13. sum of first 20 numbers
total = 0
for i in range(1, 21):
    total += i
print("Sum:", total)


# 14. star pattern
for i in range(1, 5):
    print("*" * i)


# 15. multiplication table
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 16. divisors of a number
num = 12
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()


# 17. factorial
fact = 1
num = 5
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)


# 18. prime numbers 1–50
for num in range(2, 51):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()


# 19. reverse a string
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)


# 20. count vowels in a string
s = "education"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)


# 21. pyramid pattern
for i in range(1, 4):
    print(" " * (3 - i) + "*" * (2 * i - 1))


# 22. number pattern
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 23. tables 1 to 10
for n in range(1, 11):
    for i in range(1, 11):
        print(n * i, end=" ")
    print()


# 24. factorial 1 to 10
for n in range(1, 11):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} =", fact)


# 25. count odd digits
num = 1234567
odd = 0
for d in str(num):
    if int(d) % 2 != 0:
        odd += 1
print("Odd Digits:", odd)


# 26. sum divisible by 5 (1–200)
total = 0
for i in range(1, 201):
    if i % 5 == 0:
        total += i
print("Sum divisible by 5:", total)


# 27. divisible by 3 & 7 (1–500)
for i in range(1, 501):
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=" ")
print()


# 28. fibonacci series
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 29. character frequency
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Character Count:", freq)


# 30. number pyramid
for i in range(1, 5):
    print(str(i) * i)


#   -----star patterns-----
# 1. Square Star Pattern
# for i in range(4):
#     for j in range(4):
#         print("* ", end="")
#     print()

# output-->
# * * * *
# * * * *
# * * * *
# * * * *

# 2. Right Angle Triangle (Star)
# for i in range(4):
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

# output-->
# *
# * *
# * * *
# * * * *

# 3. Inverted Right Angle Triangle
# for i in range(4):
#     for j in range(4 - i):
#         print("* ", end="")
#     print()

# output-->
# * * * *
# * * *
# * *
# *

# 4. Star Pyramid Pattern
# for i in range(4):
#     for j in range(4 - i - 1):
#         print("  ", end="")
#     for k in range(2 * i + 1):
#         print("* ", end="")
#     print()

# output-->
#       *
#     * * *
#   * * * * *
# * * * * * * *

# 5. Reverse Star Pyramid Pattern
# for i in range(4):
#     for j in range(i):
#         print("  ", end="")
#     for k in range(2 * (4 - i) - 1):
#         print("* ", end="")
#     print()

# output-->
# * * * * * * *
#   * * * * *
#     * * *
#       *


# 6. Number Square Pattern
# for i in range(4):
#     for j in range(4):
#         print(j + 1, end=" ")
#     print()

# output-->
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# 7. Number Right Angle Triangle
# for i in range(4):
#     for j in range(i + 1):
#         print(j + 1, end=" ")
#     print()

# output-->
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# 8. Repeated Number Triangle
# for i in range(4):
#     for j in range(i + 1):
#         print(i + 1, end=" ")
#     print()

# output-->
# 1
# 2 2
# 3 3 3
# 4 4 4 4


# 9. Inverted Number Triangle
# for i in range(4):
#     for j in range(4 - i):
#         print(j + 1, end=" ")
#     print()

# output-->
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# 10. Continuous Number Pattern
# num = 1
# for i in range(4):
#     for j in range(i + 1):
#         print(num, end=" ")
#         num += 1
#     print()

# output-->
# 1
# 2 3
# 4 5 6
# 7 8 9 10
