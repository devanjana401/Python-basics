#  tuples are immutable, they have very few methods compared to lists.

# Tuple example
fruits = ("apple", "banana", "cherry", "apple")
# count()
apple_count = fruits.count("apple")
print("Count of apple:", apple_count)
# index()
banana_index = fruits.index("banana")
print("Index of banana:", banana_index)

# other useful
nums = (5, 2, 8, 3, 2)
# Length
print("Length:", len(nums))
# Maximum & Minimum
print("Max:", max(nums))
print("Min:", min(nums))
# Sum of elements
print("Sum:", sum(nums))
# Membership test
print("Is 3 in tuple?", 3 in nums)
# Concatenation
new_nums = nums + (10, 20)
print("Concatenated tuple:", new_nums)
# Repetition
print("Repeated tuple:", nums * 2)