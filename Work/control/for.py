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
