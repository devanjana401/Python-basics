# adding elements
fruits = ["apple","banana"]
# append() -> add item at end
fruits.append("cherry")
print("append:",fruits)
# insert(index,value) -> add at specific position
fruits.insert(1,"mango")
print("insert:",fruits)
# extend(iterable) -> add multiple items
fruits.extend(["grape","orange"])
print("extend:",fruits)

# removing elements
fruits1 = ["apple","banana","cherry","apple"]
# remove(value) -> removes first occurence
fruits1.remove("apple")
print("remove:",fruits1)
# pop(index) -> removes item at index(default last)
fruits1.pop()
print("pop last:",fruits1)
fruits1.pop(0)
print("pop index 0:",fruits1)
# clear() -> removes all item
fruits1.clear()
print("clear:",fruits1)

# searching and counting
nums = [3, 1, 4, 2]
# sort() → ascending order
nums.sort()
print("sorted ascending:", nums)
# sort(reverse=True) → descending order
nums.sort(reverse=True)
print("sorted descending:", nums)
# reverse() → reverse the list
nums.reverse()
print("reverse:", nums)

# copying
fruits = ["apple",["banana", "cherry"]]
# copy() → shallow copy
new_list = fruits.copy()
# new_list = copy.deepcopy(fruits)
fruits[1][0]="mango"
print("fruits:", fruits)
print("copy:", new_list)

# other useful
nums = [1,2,3]
# len() → number of items
print("length:", len(nums))
# max() → maximum value
print("max:", max(nums))
# min() → minimum value
print("min:", min(nums))
# sum() → sum of elements
print("sum:", sum(nums))
# sorted(list) → returns new sorted list
print("sorted function:", sorted(nums, reverse=True))
slist=sorted(nums,reverse=True)
print(slist)
print(nums)
nums.sort(reverse=True)
print(nums)